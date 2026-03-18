#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    # Create a shallow copy of the list
    new_list = my_list[:]
    # Check index validity
    if 0 <= idx < len(new_list):
        new_list[idx] = element
    return new_list
