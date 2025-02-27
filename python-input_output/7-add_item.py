#!/usr/bin/python3
"""
Script that takes command-line arguments,
    adds them to a list,
    and saves the list to a file in JSON format.
"""

import os
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = "add_item.json"

# Load existing list from file if it exists, otherwise start with an empty list
if os.path.exists(file_name):
    my_list = load_from_json_file(file_name)
else:
    my_list = []

# Add command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(my_list, file_name)
