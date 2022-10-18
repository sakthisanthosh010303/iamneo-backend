# Author: Sakthi Santhosh
# Created on: 13/10/2022
#
# Flask Backend Server Tester - DELETE
def main(argv: list) -> int:
    if not argv:
        print("Error: Program called with no data.")
        return 1

    from requests import post

    DATA = {"uuid": argv[0]}

    try:
        request_handle = post(url="https://127.0.0.1:5000/delete", json=DATA)
        print(request_handle.json())

        request_handle.close()
        return 0
    except Exception as error:
        print("Error:", error)
        return 1

if __name__ == "__main__":
    from sys import argv

    exit(main(argv[1:]))
