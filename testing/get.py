# Author: Sakthi Santhosh
# Created on: 13/10/2022
#
# argv: search_key, search_value
#
# Flask Backend Server Tester - GET
def main(argv: list) -> int:
    from requests import get, post
    from config import URL

    try:
        if len(argv) == 2:
            request_handle = post(url=URL + "get", json={argv[0]: argv[1]})
        else:
            request_handle = get(url=URL + "get")

        print(request_handle.json())
        request_handle.close()
        return 0
    except Exception as error:
        print("Error:", error)
        return 1

if __name__ == "__main__":
    from sys import argv

    exit(main(argv[1:]))
