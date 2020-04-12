import codecs
from json import dump, loads
from BusClass import *


def serialization_object(bus_route):
    with codecs.open('bus_list.json', 'w') as file_out:
        dump(bus_route, file_out, default=lambda obj: obj.__dict__, indent=4)


def deserialization(file_name):
    with open(file_name, 'r') as f:
        data = f.read()
        json_data = BusRoute.from_json(loads(data))
    return json_data


bus1 = Bus('Moscow', 'Piter', 246, 3)
bus2 = Bus('Tashkent', 'Sochi', 321, 1)
buses = BusRoute([bus1, bus2])

serialization_object(buses)

bus = deserialization("bus_list.json")

for i in bus.bus_list:
    i.get_info()
