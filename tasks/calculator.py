# Program: Rock Paper Scissors Game
# 
# Description: Design a simple calculator with basic arithmetic operations
#              Prompt the user to input two numbers and an operation choice
#
# Author: DHLAMINI SNYMAN @ https://www.github.com/SnymanD


print("Calculator Application")
print("-----------------------")
print("")

def calculator():
    num1 = float(input("Enter The First Number: "))
    print("")
    operator = input("Choose one operator (+, -, *, /, %): ")
    print("")
    num2 = float(input("Enter The Second Number: "))
    print("")

    if operator == "+":
        print(f"{num1} + {num2} = {num1 + num2} \n")

    elif operator == "*":
        print(f"{num1} * {num2} = {num1 * num2} \n")

    elif operator == "/":
        print(f"{num1} / {num2} = {num1 / num2} \n")

    elif operator == "-":
        print(f"{num1} - {num2} = {num1 - num2} \n")

    elif operator == "%":
        print(f"{num1} % {num2} = {num1 % num2} \n")

    else:
        print(f"You have entered {operator}, choose a valid operator! \n")
        
while True:
    
    choose = int(input(f"{1}. Perform Calculations \n"
                       f"{2}. Quit \n"
                       ">>> Choose 1 or 2: "))
    print("")
    
    if choose == 1:
        calculator()
        
    elif choose == 2:
        print(f"Calculator turned off!")
        print("")
        break
    