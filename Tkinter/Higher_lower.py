from tkinter import *
import random
random_number = random.randint(1, 100)

def check_number():
    num = int(number.get())
    if num == random_number:
        response.config(text='You found it!')
    elif num < random_number:
        response.config(text='The random number is higher')
    elif num > random_number:
        response.config(text='The random number is lower')
    else:
        response.config(text='Invalid input, try again')



root = Tk()
root.geometry('300x400')

greetings = Label(root, text='Welcome to the Higher Lower Game')
greetings.pack()

information = Label(root, text='A random number between 1-100 will be generated\n'
'and you need to guess that number, hints will be provided, Good luck!')
information.pack()

number = Entry(root)
number.pack()

button = Button(root, text='Check', command= check_number)
button.pack()

response = Label(root)
response.pack()

root.mainloop()