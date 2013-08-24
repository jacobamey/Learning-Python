"""This is the "recurs_print.py" module, and it provides one function called
list_print() which prints lists that may or may not include nested lists"""


def list_print(a_list):
    """This function takes a positional argument called "a_list", which is any
     Python list (of, possibly, nested lists). Each data item in the provided list
     is (recursively) printed to the screen on its own line"""
    for each_item in a_list:
        if isinstance(each_item, list):
            list_print(each_item)
        else:
            print(each_item)