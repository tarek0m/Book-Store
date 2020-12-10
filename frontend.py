from tkinter import *
from backend import Database

database = Database("books.db")

def create_title(text, row, column):
    label = Label(window, text=text)
    label.grid(row=row, column=column)
    
def create_entry(row, column):
    e_value = StringVar()
    e = Entry(window, textvariable=e_value)
    e.grid(row=row, column=column)
    return (e, e_value)

def create_button(text, row, column, command):
    button = Button(text=text, width=15, command=command)
    button.grid(row=row, column=column)

def elemination(entry, index):
    entry.delete(0, END)
    entry.insert(END, index)

def get_selected_row(event):
    try:
        global selected_row
        #curselection() ALONE ht5aleek t5tar ely el cursor m7toot 3leeh fe el-listbox
        #which is <tuple>
        index = list_.curselection()[0]
        selected_row = list_.get(index)
        elemination(title_entry[0], selected_row[1])
        elemination(author_entry[0], selected_row[2])
        elemination(year_entry[0], selected_row[3])
        elemination(isbn_entry[0], selected_row[4])
    except IndexError:
        pass

def view_command():
    list_.delete(0, END)
    for row in database.view():
        list_.insert(END, row)

def search_command():
    list_.delete(0, END)
    for row in database.search(title_entry[1].get(), author_entry[1].get(), year_entry[1].get(), isbn_entry[1].get()):
        list_.insert(END, row)

def add_command():
    database.insert(title_entry[1].get(), author_entry[1].get(), year_entry[1].get(), isbn_entry[1].get())
    list_.delete(0, END)
    list_.insert(END, "Entry has been added successfully!")

def update_command():
    database.update(selected_row[0], title_entry[1].get(), author_entry[1].get(), year_entry[1].get(), isbn_entry[1].get())
    list_.delete(0, END)
    list_.insert(END, "Entry has been updated successfully!")

def delete_command():
    database.delete(selected_row[0])
    list_.delete(0, END)
    list_.insert(END, "Entry has been added successfully!")

#start window
window = Tk()

window.wm_title("Book Store")

#title
create_title("Title", 0, 0)
title_entry = create_entry(0, 1)

#author 
create_title("Author", 0, 2)
author_entry = create_entry(0, 3)

#year
create_title("Year", 1, 0)
year_entry = create_entry(1, 1)

#isbn
create_title("ISBN", 1, 2)
isbn_entry = create_entry(1, 3)

#view all
create_button("View All", 2, 3, view_command)

#search
create_button("Search Entry", 3, 3, search_command)

#add
create_button("Add Entry", 4, 3, add_command)

#ubdate
create_button("Update Selected", 5, 3, update_command)

#delete
create_button("Delete Selected", 6, 3, delete_command)

#close
create_button("Close", 7, 3, window.destroy)

#list
list_ = Listbox(window, height=15, width=55)
#rowspan: ana 3ayz a5od msa7et kam row
#w el-columnspan zayaha
list_.grid(row=2, column=0, rowspan=6, columnspan=2)

#scrollbar
sb = Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

#el-configration; we tell the list meen haymskha 3la el y-axis
#w b2ol ll-scrollbar htmsk el-list 3la el-y ray7 gay
list_.configure(yscrollcommand=sb.set)
sb.configure(command=list_.yview)

list_.bind('<<ListboxSelect>>', get_selected_row)

#end window
window.mainloop()