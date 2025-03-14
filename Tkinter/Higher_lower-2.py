from tkinter import *
import random

def generate_number():
    """Generates a new random number"""
    global random_number
    random_number = random.randint(1, 100)

def check_number():
    """Checks the user input against the random number"""
    try:
        num = int(number.get())
        if num == random_number:
            response.config(text='🎉 You found it! Click Reset to play again.' ,fg='green')
        elif num < random_number:
            response.config(text=f'🔼 The random number is higher than {num}', fg='blue')
        else:
            response.config(text=f'🔽 The random number is lower than {num}', fg='blue')
        number.delete(0, END)
    except ValueError:
        response.config(text='❌ Invalid input, please enter a number.', fg='red')
        
def reset_game():
    """Resets the game by generating a new number and clearing the input"""
    generate_number()
    response.config(text='New game started! Guess the number.', fg='black')
    number.delete(0, END)  # Clear input field

# Initialize game
root = Tk()
root.geometry('350x400')
root.title("Higher Lower Game")

# Generate the first number
generate_number()

# UI Elements
Label(root, text='🎮 Welcome to the Higher Lower Game!', font=("Arial", 12, "bold")).pack(pady=10)
Label(root, text='A random number between 1-100 has been generated.\nGuess the number using hints!', font=("Arial", 10)).pack(pady=5)

number = Entry(root, font=("Arial", 12))
number.pack(pady=5)

Button(root, text='Check', command=check_number, font=("Arial", 12, "bold")).pack(pady=5)
Button(root, text='Reset', command=reset_game, font=("Arial", 12, "bold")).pack(pady=5)

response = Label(root, text='', font=("Arial", 12))
response.pack(pady=10)

root.mainloop()
