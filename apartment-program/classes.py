from typing import List
import copy


class FloorPlan(object):

    def __init__(self, description: str, img: str):
        self.description = description
        self.img = img

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

    def to_string(self, num_indent=0):
        string = ""
        string += num_indent * "\t" + "Bed(s): " + str(self.bed) + "\n"
        string += num_indent * "\t" + "Bath(s): " + str(self.bath) + "\n"
        string += num_indent * "\t" + "Price: " + str(self.price) + "\n"

        # TODO: Need to accurately print out the Floor plans for each of them
        string += num_indent * "\t" + "Floor Plan: " + str(len(self.floor_plan)) + "\n"
        return string


class Amenity(object):

    def __init__(self, name: str):
        self.name = name

    @classmethod
    def from_json(cls, data: str):
        return cls(data)

    def to_string(self, num_indent=0):
        string = ""
        string += num_indent * "\t" + "-" + self.name + "\n"
        return string


class Property(object):

    def __init__(self, options: List[Option], amenities: List[Amenity], address: str, agency: str, website: str):
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
        amenities = list(map(Amenity.from_json, data["amenities"]))
        return cls(options, amenities, data["address"], data["agency"], data["website"])

    def to_string(self, num_indent=0):
        string = ""
        string += num_indent * "\t" + "Address: " + str(self.address).upper() + "\n"
        string += num_indent * "\t" + "Agency: " + str(self.agency) + "\n"

        # Print out all Option's at the Property
        string += num_indent * "\t" + "Living Options: " + "\n"
        for option in self.options:
            string += option.to_string(num_indent + 1) + "\n"

        # Print out all Amenity's at the Property
        string += num_indent * "\t" + "Amenities: " + "\n"
        for amenity in self.amenities:
            string += amenity.to_string(num_indent + 1)

        string += num_indent * "\t" + "Website: " + str(self.website) + "\n"
        return string

    def as_dict(self):
        return copy.deepcopy(self.__dict__)


class RealEstateAgency(object):

    def __init__(self, name, properties: List[Property]):
        self.name = name
        self.properties = properties

    # def construct_properties_dict(self, properties=[]):
    #     # TODO: Finish construct properties dictionary mapping addresses to Apartment objects
    #     property_dict = {}
    #     for property in properties:
    #         p = Property()
    #         property_dict[property.get_address()] = property
    #     return property_dict

    def search_properties(self, address: str):
        # TODO: Implement property search method which searches for the address within the agency
        address = address.lower()

        if address in self.properties:
            return self.properties[address]

        print("Address not found")
        return None

    def get_name(self):
        return self.name

    def get_properties(self):
        return self.properties

    @classmethod
    def from_json(cls, data: dict):
        properties = list(map(Property.from_json, data["properties"]))
        return cls(data["name"], properties)

    def to_string(self, num_indent=0):
        string = ""

        # Name
        string += num_indent * "\t" + "Management Agency: " + str(self.name) + "\n"

        # Properties
        for property in self.properties:
            string += property.to_string(num_indent + 1) + "\n"

            # Separate the properties
            string += 80 * "-"
            string += 2 * "\n"

        # Separate between different Management Groups
        string += 80*"="
        string += "\n"

        return string

# TODO: Make all to_string methods into an interface and have classes implement
# TODO: Method to add in a new property under agency and append to json.
