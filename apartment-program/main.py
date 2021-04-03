# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from json_parser import *

def search_property(address, agency=None):
    # # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    file_path = "./testing.json"
    output_file_path = "output.txt"

    print(JsonApartmentParser.parse_json(file_path), file=open(output_file_path, "w"))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
