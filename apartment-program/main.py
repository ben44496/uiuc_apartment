# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import json
from classes import *

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    file_path = "./testing.json"
    with open(file_path, "r") as file:
        decoded_floor_plan = Apartment.from_json(json.loads(file.read()))
        # data = json.loads(file.read())
        # print(data)
    print(decoded_floor_plan.to_string(0))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
