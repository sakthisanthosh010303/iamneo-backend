# Author: Sakthi Santhosh
# Created on: 01/12/2022
#
# Database Backup Tool
def main() -> int:
    from shutil import copy2

    try:
        copy2("./static/database.db", "./static/database.db.save")
    except Exception as error:
        print("Error:", error)
        return 1
    else:
        print("Info: Database backup made sucessfully.")
    return 0

if __name__ == "__main__":
    exit(main())
