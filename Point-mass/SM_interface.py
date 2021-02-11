#To create an .EXE file, go to terminal and execute pyinstaller --clean --onefile SM_interface.spec

# Importing everything from tkinter
from tkinter import *

# Creating window project
window = Tk()

# Define 4 labels
l1 = Label(window, text = "Title")
l1.grid(row = 0, column = 0)

l2 = Label(window, text = "Author")
l2.grid(row = 0, column = 2)

l3 = Label(window, text = "Year")
l3.grid(row = 1, column = 0)

l4 = Label(window, text = "ISBN")
l4.grid(row = 1, column = 2)

# Define entries
title_text = StringVar()
e1 = Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)

author_text = StringVar()
e2 = Entry(window, textvariable = author_text)
e2.grid(row = 0, column = 3)

year_text = StringVar()
e3 = Entry(window, textvariable = year_text)
e3.grid(row = 1, column = 1)

isbn_text = StringVar()
e4 = Entry(window, textvariable = isbn_text)
e4.grid(row = 1, column = 3)

# Define ListBox

list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

# Attach scrollbar to the list

sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, columnspan = 6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

# Define Buttons
b1 = Button(window, text = "Os cara", width = 12)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "são", width = 12)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "foda", width = 12)
b3.grid(row = 4, column = 3)


window.mainloop()
