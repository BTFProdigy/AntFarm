# DEFINITIONS
class PoundError(Exception):
    def __init__(self):
        print("Exception raised because '#' found.")


def get_name():
    print("Please enter a name (if it contains a '#', an error message will appear: ")
    name_input = input()
    if name_input.find('#') > -1:
        raise PoundError()

try:
    get_name()
except Exception:
    pass