# Author: Sakthi Santhosh
# Created on: 12/10/2022
#
# Backend Flask Application
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from json import dumps
from os import system
from sqlite3 import connect, Row
from uuid import uuid4
from werkzeug.exceptions import HTTPException

def get_entry(json: dict) -> dict:
    try:
        with connect("./static/db_final.db") as database_handle:
            database_handle.row_factory = Row
            cursor = database_handle.cursor()
            if json:
                search_key = tuple(json.keys())[0]
                if search_key not in (
                    "uuid", "name", "email", "password", "dob", "address", "phone", "image"):
                        raise Exception(
                            "Field with name '%s' not found."%(search_key))
                cursor.execute("""
                    SELECT * FROM randomdb WHERE \"%s\"=\"%s\" LIMIT 1
                """%(search_key, json[search_key]))
            else:
                cursor.execute("""
                    SELECT * FROM randomdb ORDER BY RANDOM() LIMIT 1
                """)
            data = cursor.fetchone()
        if data:
            return dict(data)
        else:
            raise Exception(
                "Entry with data '%s' not found."%(json[update_key]))
    except Exception as error:
        print("Error:", error)
        return {
            "get": False,
            "description": str(error)
        }

def restore_db() -> dict:
    try:
        system("cp ./static/db_final.db.save ./static/db_final.db")
        return {"restore": True}
    except Exception as error:
        return {
            "restore": False,
            "description": str(error)
        }


def ins_entry(json: dict) -> dict:
    try:
        uuid = str(uuid4())
        with connect("./static/db_final.db") as database_handle:
            cursor = database_handle.cursor()
            cursor.execute("""
                INSERT INTO randomdb VALUES(
                    \"%s\", \"%s\", \"%s\", \"%s", \"%s\", \"%s\", \"%s\", \"%s\"
                )"""%(
                uuid,
                json["name"],
                json["email"],
                json["password"],
                json["dob"],
                json["address"],
                json["phone"],
                json["image"]
            ))
            database_handle.commit()
        return {
            "post": True,
            "uuid": uuid
        }
    except Exception as error:
        print("Error:", error)
        return {
            "post": False,
            "description": str(error)
        }

def upd_entry(json: dict) -> dict:
    try:
        update_key = tuple(json.keys())[1]
        if update_key not in (
            "name", "email", "password", "dob", "address", "phone", "image"):
                raise Exception(
                    "Field with name '%s' not found."%(update_key))
        with connect("./static/db_final.db") as database_handle:
            cursor = database_handle.cursor()
            cursor.execute("""
                    SELECT * FROM randomdb WHERE uuid=\"%s\"
            """%(json["uuid"]))
            if not cursor.fetchone():
                raise Exception("Entry with UUID '%s' not found."%(json["uuid"]))
            cursor.execute("""
                UPDATE randomdb SET %s=\"%s\" WHERE uuid=\"%s\"
            """%(update_key, json[update_key], json["uuid"]))
            database_handle.commit()
        return {"patch": True}
    except Exception as error:
        print("Error:", error)
        return {
            "patch": False,
            "error": str(error)
        }

def del_entry(uuid: str) -> dict:
    try:
        with connect("./static/db_final.db") as database_handle:
            cursor = database_handle.cursor()
            cursor.execute("""
                    SELECT * FROM randomdb WHERE uuid=\"%s\"
            """%(uuid))
            if not cursor.fetchone():
                raise Exception("Entry with UUID '%s' not found."%(uuid))
            cursor.execute("""
                DELETE FROM randomdb WHERE uuid=\"%s\"
            """%(uuid))
            database_handle.commit()
        return {"delete": True}
    except Exception as error:
        print("Error:", error)
        return {
            "delete": False,
            "description": str(error)
        }

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
    return render_template("index.html")

@app.route("/get", methods=["GET", "POST"])
@cross_origin(support_credentials=True)
def get_handle() -> dict:
    if request.method == "POST":
        return get_entry(request.get_json())
    else:
        return get_entry({})

@app.route("/restore", methods=["GET"])
def restore_handle() -> dict:
    return restore_db()

@app.route("/post", methods=["POST"])
def post_handle() -> dict:
    return ins_entry(request.get_json())

@app.route("/patch", methods=["PATCH"])
def patch_handle() -> dict:
    return upd_entry(request.get_json())

@app.route("/delete", methods=["POST"])
def delete_handle() -> dict:
    return del_entry(request.get_json()["uuid"])

@app.errorhandler(HTTPException)
def error_handle(error):
    return render_template("error.html", data={
        "code": error.code,
        "name": error.name,
        "description": error.description,
    })

if __name__ == "__main__":
    app.run(debug=False)
