from tkinter import *

def display():
    print('Button clicked')

root = Tk()
root.geometry('300x400')

# if i want to make the button do stuff i change the command parameter
# the passed function shouldn't be put with () to avoid immediate function call
button = Button(root, text='Click Here', command=display)
button.pack()
root.mainloop()