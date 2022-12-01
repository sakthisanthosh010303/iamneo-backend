# Author: Sakthi Santhosh
# Created on: 13/10/2022
#
# argv: uuid
#
# Flask Backend Server Tester - DELETE
def main(argv: list) -> int:
    if not argv:
        print("Error: Program called with no data.")
        return 1

    from requests import post
    from config import URL

    DATA = {"uuid": argv[0]}

    try:
        request_handle = post(url=URL + "delete", json=DATA)
        print(request_handle.json())

        request_handle.close()
        return 0
    except Exception as error:
        print("Error:", error)
        return 1

if __name__ == "__main__":
    from sys import argv

    exit(main(argv[1:]))
