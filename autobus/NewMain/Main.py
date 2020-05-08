import tkinter as tk
from tkinter import ttk
import sqlite3


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file='add.gif')
        btn_open_dialog = tk.Button(toolbar, text='Добавить', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        btn_edit_dialog = tk.Button(toolbar, text='Редактировать', bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.LEFT)

        btn_delete = tk.Button(toolbar, text='Удалить', bg='#d7d8e0', bd=0,
                               compound=tk.TOP, command=self.delete_records)
        btn_delete.pack(side=tk.LEFT)

        btn_search = tk.Button(toolbar, text='Поиск', bg='#d7d8e0', bd=0,
                               compound=tk.TOP, command=self.open_search_dialog)
        btn_search.pack(side=tk.LEFT)

        btn_refresh = tk.Button(toolbar, text='Обновить', bg='#d7d8e0', bd=0,
                                compound=tk.TOP, command=self.view_records)
        btn_refresh.pack(side=tk.LEFT)

        btn_sort = tk.Button(toolbar, text='Сортировать', bg='#d7d8e0', bd=0,
                             compound=tk.TOP, command=self.sort_records)
        btn_sort.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('ID', 'start', 'finish', 'number', 'time'), height=15, show='headings')

        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('start', width=150, anchor=tk.CENTER)
        self.tree.column('finish', width=150, anchor=tk.CENTER)
        self.tree.column('number', width=150, anchor=tk.CENTER)
        self.tree.column('time', width=150, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('start', text='Отправление')
        self.tree.heading('finish', text='Прибытие')
        self.tree.heading('number', text='Номер маршрута')
        self.tree.heading('time', text='Время пути')

        self.tree.pack()

    def records(self, start, finish, number, time):
        self.db.insert_data(start, finish, number, time)
        self.view_records()

    def update_record(self, start, finish, number, time):
        self.db.c.execute('''UPDATE bus_routes SET start=?, finish=?, number=?, time=? WHERE ID=?''',
                          (start, finish, number, time, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM bus_routes''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM bus_routes WHERE id=?''', (self.tree.set(selection_item, '#1'),))
        self.db.conn.commit()
        self.view_records()

    def search_records(self, start):
        start = ('%' + start + '%',)
        self.db.c.execute('''SELECT * FROM bus_routes WHERE start LIKE ?''', start)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def sort_records(self):
        self.db.c.execute("SELECT * FROM bus_routes ORDER BY number ASC")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить маршрут')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_start = tk.Label(self, text='Отправление:')
        label_start.place(x=50, y=50)
        label_finish = tk.Label(self, text='Прибытие:')
        label_finish.place(x=50, y=80)
        label_num = tk.Label(self, text='Номер маршрута:')
        label_num.place(x=50, y=110)
        label_time = tk.Label(self, text='Время пути:')
        label_time.place(x=50, y=140)

        self.entry_start = ttk.Entry(self)
        self.entry_start.place(x=200, y=50)

        self.entry_finish = ttk.Entry(self)
        self.entry_finish.place(x=200, y=80)

        self.entry_num = ttk.Entry(self)
        self.entry_num.place(x=200, y=110)

        self.entry_time = ttk.Entry(self)
        self.entry_time.place(x=200, y=140)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_start.get(),
                                                                       self.entry_finish.get(),
                                                                       self.entry_num.get(),
                                                                       self.entry_time.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title('Редактировать позицию')
        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=183, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_start.get(),
                                                                          self.entry_finish.get(),
                                                                          self.entry_num.get(),
                                                                          self.entry_time.get()))

        self.btn_ok.destroy()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title('Поиск')
        self.geometry('300x100+400+300')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Поиск')
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Поиск')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('bus_routes.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS bus_routes 
            (id integer primary key, start text, finish text, number integer, time integer)''')
        self.conn.commit()

    def insert_data(self, start, finish, number, time):
        self.c.execute('''INSERT INTO bus_routes(start, finish, number, time) VALUES (?, ?, ?, ?)''',
                       (start, finish, number, time))
        self.conn.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Список маршрутов")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
