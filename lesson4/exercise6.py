# -*- coding: utf-8 -*-
# Level 2
# sixth exercise

import requests
import json

from requests.auth import HTTPBasicAuth
import xmltodict
from collections import OrderedDict


LOGIN = 'https://python-for-qa.herokuapp.com/login'
URL = 'https://python-for-qa.herokuapp.com/data'

USER = 'admin'
PASSWORD = 'password'


def main():

    response = requests.get(LOGIN, auth=HTTPBasicAuth(USER, PASSWORD)).json()
    TOKEN = response['token']

    header_for_xml = {'X-AUTH-TOKEN': TOKEN,
              "Accept": "application/xml"}
    header = {'X-AUTH-TOKEN': TOKEN}

    json_response = requests.get(URL, headers=header)
    xml_response = requests.get(URL, headers=header_for_xml)

    with open('output.json', 'w') as to2_file:
        json.dump(json_response.json(), to2_file, indent=2)

    with open('output.xml', 'w') as to_file:
        to_file.write(xml_response.text)


if __name__ == '__main__':
    main()


def comparator(data1, data2):
    for d1, d2 in zip(data1, data2):
        for key, value in d1.items():
            if value.lower().replace('\r\n', '') != (d2[key].lower().replace('\r\n', '')):
                print (key, value, (d2[key]))

datalist_xml = datalist_json = []

with open('output.xml') as f:
    d = xmltodict.parse(f)
    items = d.get('items')
    item = items.get('item')

with open('output.json', 'r') as js:
    the_dict = json.loads(js.read(),  object_pairs_hook=OrderedDict)

datalist_xml = [OrderedDict((str(k), str(v)) for (k, v) in i.items()) for i in item]
datalist_json = [OrderedDict((str(k), str(v)) for (k, v) in i.items()) for i in the_dict]

comparator(datalist_xml, datalist_json)
