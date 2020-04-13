import codecs
from json import dump, loads
from BusClass import *


def sort_list(lst):
    pass


def search_route(list_route, search):
    find_route = []
    for route in list_route:
        if route.strting_point == search or route.final_point == search:
            find_route.append(route)
    return find_route


def serialization_object(bus_route):
    with codecs.open('bus_list.json', 'w') as file_out:
        dump(bus_route, file_out, default=lambda obj: obj.__dict__, indent=4)


def deserialization(file_name):
    with open(file_name, 'r') as f:
        data = f.read()
        json_data = BusRoute.from_json(loads(data))
    return json_data
