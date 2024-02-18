"""A password generator is a useful tool that generates strong and random passwords for users. This project aims to create a password generator application using Python, allowing users to specify the length and complexity of the password.
"""
# User Input: Prompt the user to specify the desired length of the password.
# Generate Password: Use a combination of random characters to generate a password of the specified length.
# Display the Password: Print the generated password on the screen.

from tkinter import *
import string
import pyperclip
import random


def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    weak = small_alphabets
    medium = small_alphabets + capital_alphabets
    strong = small_alphabets + capital_alphabets + numbers + special_characters
    password_length = int(length_Box.get())

    if choice.get() == 1:
        passwordField.insert(0, random.sample(weak, password_length))

    if choice.get() == 2:
        passwordField.insert(0, random.sample(medium, password_length))

    if choice.get() == 3:
        passwordField.insert(0, random.sample(strong, password_length))


def copy():
    random_password = passwordField.get()
    pyperclip.copy(random_password)


root = Tk()
root.config(bg="LightBlue")
choice = IntVar()
Font_1 = ('Arial Black', 22, 'bold')
Font_2 = ('Arial', 14, 'bold')
passwordLabel = Label(root, text='Password Generator', font=Font_1, bg='LightBlue', fg='Black')
passwordLabel.grid(pady=10)
weakRadioButton = Radiobutton(root, text='Weak', value=1, width=7, variable=choice, font=Font_2, bg='Blue')
weakRadioButton.grid(pady=6)

mediumRadioButton = Radiobutton(root, text='Medium', value=2, width=7, variable=choice, font=Font_2, bg='Blue')
mediumRadioButton.grid(pady=6)

strongRadioButton = Radiobutton(root, text='Strong', value=3, width=7, variable=choice, font=Font_2, bg='Blue')
strongRadioButton.grid(pady=6)

lengthLabel = Label(root, text='Password Length', font=Font_1, bg='LightBlue', fg='Black')
lengthLabel.grid(pady=6)

length_Box = Spinbox(root, from_=3, to=30, width=7, font=Font_2)
length_Box.grid(pady=6)

generateButton = Button(root, text='Generate', width=7, font=Font_2, command=generator, borderwidth=5, bg='Blue')
generateButton.grid(pady=6)

passwordField = Entry(root, width=26, bd=2, font=Font_2)
passwordField.grid()

copyButton = Button(root, text='Copy Password', font=Font_2, command=copy, width=12, borderwidth=5, bg='Blue')
copyButton.grid(pady=6)

root.mainloop()
