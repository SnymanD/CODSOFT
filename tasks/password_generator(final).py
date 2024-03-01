# Program: Random Password Generator
# 
# Description: Asking a user to enter the length and the complexity of the password before generating one
#
# Author: DHLAMINI SNYMAN @ https://www.github.com/SnymanD

import random
import string

print("Password Generator Application")
print("______________________________")
print("")

small_alphabets = string.ascii_lowercase
capital_alphabets = string.ascii_uppercase
numbers = string.digits
special_characters = string.punctuation

weak_password = small_alphabets
medium_password = small_alphabets + capital_alphabets
strong_password = small_alphabets + capital_alphabets + numbers + special_characters


def generator():
    
    password_len = int(input("Enter The Length Of The Password You Want: "))
    print("")
    print("Choose the complexity of the password (number only):")
    choice = int(input(f"{1}. Weak Password \n"
                   f"{2}. Medium Password \n"
                   f"{3}. Strong Password \n"
                   ">>> "))
    print("")

    password = ""
    
    if choice == 1:
        password += random.choice(weak_password)
        password = ''.join([random.choice(weak_password) for i in range(password_len)])
        print(f"Your random password with {password_len} characters is: {password}")
        print("")
        
    elif choice == 2:
        password += random.choice(medium_password)
        password = ''.join([random.choice(medium_password) for i in range(password_len)])
        print(f"Your random password with {password_len} characters is: {password}")
        print("")
        
    elif choice == 3:
        password += random.choice(strong_password)
        password = ''.join([random.choice(strong_password) for i in range(password_len)])
        print(f"Your random password with {password_len} characters is: {password}")
        print("")
        
    else:
        quit
    
        
while True:
    
    choose = int(input(f"{1}. Generate A Password \n"
                       f"{2}. Quit \n"
                       ">>> Choose 1 or 2: "))
    print("")
    
    if choose == 1:
        generator()
        
    elif choose == 2:
        break
