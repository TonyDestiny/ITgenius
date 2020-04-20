import codecs
from json import dump, loads
from BusClass import *


def sort_list(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        less = [i for i in lst[1:] if i.number_of_route <= pivot.number_of_route]
        greater = [i for i in lst[1:] if i.number_of_route > pivot.number_of_route]

        return sort_list(less) + [pivot] + sort_list(greater)


def search_route(list_route, search):
    find_route = []
    for route in list_route:
        if route.starting_point == search or route.final_point == search:
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
