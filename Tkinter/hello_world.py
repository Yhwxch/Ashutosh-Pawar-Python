from tkinter import *
'''
Tk() initializes the main window of the application.
root is the main window object that will hold all GUI components.
'''
root = Tk() # window object
# we have to make the window running all time -> putting inside a loop, because once the program ends executing it will discard the window

#Setting Window Size
root.geometry('300x400')


hello = Label(root, text='Hello world')

#.pack(): Automatically arranges the label in the window
hello.pack()



'''
It starts the GUI event loop, which listens for user actions (like clicking buttons or resizing the window).
Without mainloop(), the window would open and immediately close.
'''
root.mainloop()