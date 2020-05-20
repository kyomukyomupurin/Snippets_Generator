import json
import os
from os.path import join
from pathlib import Path
import re

root_dir = '.'
output_file = './output.json'
extension_list = ['.cc', '.cpp']


def make_cpp_list() -> list:
    result = []

    for root, dirs, files in os.walk(root_dir):
        for file_name in files:
            if Path(file_name).suffix in extension_list:
                result.append(join(root, file_name))

    return result


def make_dict(file_path: str) -> dict:
    snippets_content = {}
    snippets_content["prefix"] = Path(file_path).stem
    body_list = []

    with open(file_path) as f:
        lines = f.readlines()
        start = False

        for line in lines:
            if line == '// snippet-end\n':
                break
            elif line == '// snippet-begin\n':
                start = True
            elif start:
                body_list.append(line)

    snippets_content["body"] = body_list

    return snippets_content


if __name__ == '__main__':
    json_content = {}
    cpp_file_list = make_cpp_list()

    for cpp_file in cpp_file_list:
        if make_dict(cpp_file)["body"]:
            json_content[Path(cpp_file).stem] = make_dict(cpp_file)

    with open(output_file, 'w') as of:
        of.write(json.dumps(json_content, indent=4))
