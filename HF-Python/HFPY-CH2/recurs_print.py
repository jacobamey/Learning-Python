"""This is the "recurs_print.py" module, and it provides one function called
list_print() which prints lists that may or may not include nested lists"""


def list_print(a_list, indent=False, level=0):
    """This function takes a positional argument called "a_list", which is any
     Python list (of, possibly, nested lists). Each data item in the provided list
     is (recursively) printed to the screen on its own line
     A second argument called "level" is used to insert tab-stops when a nested list is encountered.
      the 3rd argument indent which can be True or False allows the user to ignore or use the level
      (Indent feature)"""
    for each_item in a_list:
        if isinstance(each_item, list):
            list_print(each_item, indent, level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='')
            print(each_item)