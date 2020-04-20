class Bus(object):

    def __init__(self,
                 starting_point=None,
                 final_point=None,
                 number_of_route=None,
                 travel_time=None):
        self.starting_point = starting_point
        self.final_point = final_point
        self.number_of_route = int(number_of_route)
        self.travel_time = travel_time

    def get_info(self):
        # print("--------------------------------------")
        # print(f"The bus follows the route {self.number_of_route}")
        # print(f"{self.starting_point} -> {self.final_point}")
        # print(f"Travel time is {self.travel_time}")
        # print("--------------------------------------")
        string = ('--------------------------------------\n'
                  f'The bus follows the route {self.number_of_route}\n'
                  f'{self.starting_point} -> {self.final_point}\n'
                  f"Travel time is {self.travel_time}\n"
                  '--------------------------------------\n')
        return string

    def set_starting(self, starting):
        self.starting_point = starting

    def set_final(self, final):
        self.final_point = final

    def set_number(self, number):
        self.number_of_route = int(number)

    def set_time(self, time):
        self.travel_time = time

    def set_all(self,
                starting_point,
                final_point,
                number_of_route,
                travel_time):
        self.starting_point = starting_point
        self.final_point = final_point
        self.number_of_route = number_of_route
        self.travel_time = travel_time

    @classmethod
    def from_json(cls, data: dict):
        return cls(**data)


class BusRoute(object):

    def __init__(self):
        self.bus_list = []

    def add_bus(self, bus):
        self.bus_list.append(bus)

    def quick_sort(self, lst):
        if len(lst) < 2:
            return lst
        else:
            pivot = lst[0]
            less = [i for i in lst[1:] if i.number_of_route <= pivot.number_of_route]
            greater = [i for i in lst[1:] if i.number_of_route > pivot.number_of_route]

            return self.quick_sort(less) + [pivot] + self.quick_sort(greater)

    def sort_routes(self):
        self.bus_list = self.quick_sort(self.bus_list)[::-1]

    @classmethod
    def from_json(cls, data: dict):
        bus_obj = cls()
        bus_list = list(map(Bus.from_json, data["bus_list"]))
        for bus in bus_list:
            bus_obj.add_bus(bus)
        return bus_obj
