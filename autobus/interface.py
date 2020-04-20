from tkinter import *
from util import *

buses = BusRoute()


def search():
    bus = search_entry.get()
    if bus:
        finder = search_route(buses.bus_list, bus)
        print_route(finder)


def print_route(lst):
    table.delete('1.0', END)
    for bus in lst:
        string = bus.get_info()
        table.insert(END, string)


def add_bus_route():
    bus_temp = Bus(start_str.get(), finish_str.get(), route_str.get(), time_str.get())
    buses.add_bus(bus_temp)
    start_city.delete(0, 'end')
    final_city.delete(0, 'end')
    num_route.delete(0, 'end')
    time_travel.delete(0, 'end')


root = Tk()
root.geometry("600x400")
root.title("Rout table")

start_str = StringVar()
finish_str = StringVar()
route_str = StringVar()
time_str = StringVar()
search_str = StringVar()

lb_start = Label(root, text="Departure point").place(x=100, y=0)
lb_finish = Label(root, text="Destination point").place(x=100, y=25)
lb_route = Label(root, text="Route number").place(x=100, y=50)
lb_time = Label(root, text="Route time").place(x=100, y=75)

start_city = Entry(root, width=10, textvariable=start_str)
final_city = Entry(root, width=10, textvariable=finish_str)
num_route = Entry(root, width=10, textvariable=route_str)
time_travel = Entry(root, width=10, textvariable=time_str)
search_entry = Entry(root, width=10, textvariable=search_str)

start_city.place(x=0, y=0)
final_city.place(x=0, y=25)
num_route.place(x=0, y=50)
time_travel.place(x=0, y=75)
search_entry.place(x=0, y=150)

sort_bt = Button(text='Sort', font='16', width=5, command=buses.sort_routes).place(x=515, y=100)
search_bt = Button(text='Search', font='16', width=5, command=search).place(x=5, y=175)
print_bt = Button(text='Print routes', font='16', command=lambda: print_route(buses.bus_list)).place(x=270, y=100)
add_bt = Button(text="Add", fg="green", font="16", width=5, command=add_bus_route).place(x=0, y=100)
delete_bt = Button(text="Delete", fg="red", font="16", width=5).place(x=85, y=100)
change_bt = Button(text="Change", font="16", width=5).place(x=170, y=100)
write_bt = Button(text='Write in file', bg='yellow', font='16',
                  command=lambda: serialization_object(buses)).place(x=70, y=350)


table = Text(width=40, height=15)
table.place(x=270, y=135)

root.mainloop()
