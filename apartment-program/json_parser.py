import json
from classes import *


class JsonApartmentParser:

    @staticmethod
    def parse_json(file_path: str):
        with open(file_path, "r") as file:
            decoded_json = json.loads(file.read())
            string = ""
            for agency in decoded_json:
                agency_object = RealEstateAgency.from_json(decoded_json[agency])
                string += agency_object.to_string()
            return string
        return None

