#!/usr/bin/python3
""" Module that adds all arguments to a Python list, and then
save them to a file
"""

import sys
import os.path


save_file = __import__('5-save_to_json_file.py').save_to_json_file  """ Save file function """
load_file = __import__('6-load_from_json_file.py').load_from_json_file """ Load file function """

my_list = []
if os.path.exists("add_item.json"):
    my_list = load_file("add_item.json")

for arg in sys.argv[1:]:
    my_list.append(arg)

save_file(my_list, "add_item.json")
""" Save file function """
