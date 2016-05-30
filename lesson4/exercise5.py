# Level 2
# fifth exercise

import json
import requests
from requests.auth import HTTPBasicAuth

ENDPOINT = 'https://python-for-qa.herokuapp.com/login'


def main():
    with open('clients.json', 'r') as from_file:
        reader = json.loads(from_file.read())

        for item in reader:
            USER = item["name"]
            PASSWORD = item["password"]

            response = requests.get(ENDPOINT, auth=HTTPBasicAuth(USER, PASSWORD))
            if response.status_code == 401:
                print ("Unauthorized Access - {}, {}".format(USER, PASSWORD))


if __name__ == '__main__':
    main()
