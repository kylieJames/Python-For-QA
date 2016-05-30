# coding=utf-8
# Level 1
# second exercise

import json


def replace_owner(input_file, output_file, new_owner):
    with open(input_file, 'r') as from_file:
        reader = json.loads(from_file.read())

        for item in reader:
            item["Owner"] = new_owner

        with open(output_file, 'w') as to_file:
            json.dump(reader, to_file, indent=2)

replace_owner('bugs.json', 'bugs_new.json', 'qa5')