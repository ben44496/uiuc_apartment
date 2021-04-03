import json
from classes import *


class JsonApartmentParser:

    @staticmethod
    def parse_json(file_path: str):
        with open(file_path, "r") as file:
            decoded_json = json.loads(file.read())
            mhm = RealEstateAgency.from_json(decoded_json["MHM"])
            return mhm.to_string()
        return None


if __name__ == '__main__':
    # print_hi('PyCharm')
    file_path = "./testing.json"
    with open(file_path, "r") as file:
        decoded_floor_plan = Property.from_json(json.loads(file.read()))
        # data = json.loads(file.read())
        # print(data)
    print(decoded_floor_plan.to_string(0))
