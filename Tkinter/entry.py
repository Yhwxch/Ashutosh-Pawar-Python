from tkinter import *

def display():
    # this will return whichever the data or the input from user in the entry
    data = entry.get()
    # then i will display the data to terminal 
    print(data)

root = Tk()
root.geometry('300x400')

# for user input field we call the Entry object
entry = Entry(root)
entry.pack()


button = Button(root, text='Click Here', command=display)
button.pack()
root.mainloop()