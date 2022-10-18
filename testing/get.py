# Author: Sakthi Santhosh
# Created on: 13/10/2022
#
# Flask Backend Server Tester - GET
def main(argv: list) -> int:
    from requests import get, post

    URL = "http://127.0.0.1:5000/get"

    try:
        if argv:
            request_handle = post(url=URL, json={argv[0]: argv[1]})
        else:
            request_handle = get(url=URL)

        print(request_handle.json())
        request_handle.close()
        return 0
    except Exception as error:
        print("Error:", error)
        return 1

if __name__ == "__main__":
    from sys import argv

    exit(main(argv[1:]))
