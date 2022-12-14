# Author: Sakthi Santhosh
# Created on: 13/10/2022
#
# argv: uuid, key, new_value
#
# Flask Backend Server Tester - PATCH
def main(argv: list) -> int:
    if len(argv) < 3:
        print("Error: Program called with no data.")
        return 1

    from requests import patch
    from config import URL

    DATA = {
        "uuid": argv[0],
        argv[1]: argv[2]
    }

    try:
        request_handle = patch(url=URL + "patch", json=DATA)
        print(request_handle.json())

        request_handle.close()
        return 0
    except Exception as error:
        print("Error:", error)
        return 1

if __name__ == "__main__":
    from sys import argv

    exit(main(argv[1:]))
