from tkinter import *

def selected():
    sugar = sugar_var.get()
    ice = ice_var.get()
    cream = cream_var.get()

root = Tk()
root.geometry('300x400')


sugar_var = BooleanVar()
ice_var = BooleanVar()
cream_var = BooleanVar()

sugar_checkbox = Checkbutton(root, text='Sugar', variable=sugar_var, command=selected)

ice_checkbox = Checkbutton(root, text='Ice', variable=ice_var, command=selected)

cream_checkbox = Checkbutton(root, text='Cream', variable=cream_var, command=selected)

label = Label(root)


sugar_checkbox.pack()
ice_checkbox.pack()
cream_checkbox.pack()
label.pack

root.mainloop()