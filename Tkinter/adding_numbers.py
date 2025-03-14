from tkinter import *

def add():
    # the entry field saves the input as string so we need to cast int
    n1 = int(num1.get())
    n2 = int(num2.get())
    result = n1 + n2
    answer.config(text=f'Answer is: {result}')

root = Tk()
root.geometry('300x400')

num1 = Entry(root)
num2 = Entry(root)
num1.pack()
num2.pack()

button = Button(root, text='Add', command= add)
button.pack()

answer = Label(root)
answer.pack()

root.mainloop()