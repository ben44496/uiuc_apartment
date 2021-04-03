from typing import List


class FloorPlan(object):

    def __init__(self):
        self.description = ""
        self.img = ""

    @classmethod
    def from_json(cls, data: dict):
        return cls(**data)


class Option(object):

    def __init__(self, bed: int, bath: int, price: float, floor_plan: List[FloorPlan]):
        self.bed = bed
        self.bath = bath
        self.price = price
        self.floor_plan = floor_plan

    @classmethod
    def from_json(cls, data: dict):
        return cls(**data)

    def to_string(self, num_indent):
        string = ""
        string += num_indent * "\t" + "Bed(s): " + str(self.bed) + "\n"
        string += num_indent * "\t" + "Bath(s): " + str(self.bath) + "\n"
        string += num_indent * "\t" + "Price: " + str(self.price) + "\n"

        # TODO: Need to accurately print out the Floor plans for each of them
        string += num_indent * "\t" + "Floor Plan: " + str(len(self.floor_plan)) + "\n"
        return string


class Apartment(object):

    def __init__(self, options: List[Option], amenities: List[str], address: str, agency: str,  website: str):
        # options: List[Option], amenities: List[str],
        self.address = address
        self.agency = agency
        self.options = options
        self.amenities = amenities
        self.website = website

    @classmethod
    def from_json(cls, data: dict):
        # students = list(map(Student.from_json, data["students"]))
        options = list(map(Option.from_json, data["options"]))
        amenities = list(map(str, data["amenities"]))
        return cls(options, amenities, data["address"], data["agency"], data["website"])
        # return cls(**data)

    def to_string(self, num_indent):
        string = ""
        string += num_indent * "\t" + "Address: " + str(self.address) + "\n"
        string += num_indent * "\t" + "Agency: " + str(self.agency) + "\n"

        string += num_indent * "\t" + "Living Options: " + "\n"
        # print(type(self.options[0]))
        for option in self.options:
            string += option.to_string(num_indent+1) + "\n"

        string += num_indent * "\t" + "Amenities: " + "\n"
        # TODO Should I make an ameneties class that just holds a list? Also weighted?
        for amenity in self.amenities:
            string += (num_indent+1) * "\t" + "-"+str(amenity) + "\n"

        string += num_indent * "\t" + "Website: " + str(self.website) + "\n"
        return string


class RealEstateAgency(object):

    def __init__(self, name, properties: List[Apartment]):
        self.name = name
        self.properties_dict = self.construct_properties_dict(properties);

    def construct_properties_dict(self, properties=[]):
        # TODO: Finish construct properties dictionary mapping addresses to Apartment objects
        property_dict = {}
        for property in properties:
            p = Apartment()
            property_dict[property.get_address()] = property
        return property_dict

    def search_properties(self, address):
        if address in self.properties_dict:
            return self.properties_dict[address]
        print("Address not found")
        return None

    def get_name(self):
        return self.name

    def get_properties(self):
        return self.properties
