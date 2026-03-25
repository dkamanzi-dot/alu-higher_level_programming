#!/usr/bin/python3
"""Script that adds arguments to a list and saves to a JSON file."""

import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Safely try to load existing data; if file doesn't exist, use empty list
if os.path.exists(filename):
    try:
        items = load_from_json_file(filename)
    except Exception:
        items = []
else:
    items = []

# Append command line arguments
items.extend(sys.argv[1:])

# Save updated list
save_to_json_file(items, filename)
