from tkinter import *
from util import *

buses = BusRoute()


def create_bus_route():
    bus_temp = Bus(starting_point=start_city.get(),
                   final_point=final_city.get(),
                   number_of_route=num_route.get(),
                   travel_time=time_travel.get())
    buses.add_bus(bus_temp)


root = Tk()
root.geometry("600x400")
root.title("Rout table")

lb_start = Label(text="Departure point").place(x=100, y=0)
lb_finish = Label(text="Destination point").place(x=100, y=25)
lb_route = Label(text="Route number").place(x=100, y=50)
lb_time = Label(text="Route time").place(x=100, y=75)

start_city = Entry(width=10).place(x=0, y=0)
final_city = Entry(width=10).place(x=0, y=25)
num_route = Entry(width=10).place(x=0, y=50)
time_travel = Entry(width=10).place(x=0, y=75)

save_bt = Button(text="Save", fg="green", font="16", width=5, command=create_bus_route).place(x=0, y=100)
delete_bt = Button(text="Delete", fg="red", font="16", width=5).place(x=85, y=100)
change_bt = Button(text="Change", font="16", width=5).place(x=170, y=100)

table = Text(width=40, height=15).place(x=270, y=135)

root.mainloop()
