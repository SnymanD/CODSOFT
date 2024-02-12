# Design a simple calculator with basic arithmetic operations
# Prompt the user to input two numbers and an operation choice
# Perform the calculation and display the result

print("Calculator Application")
print("----------------------")

num1 = int(input("Enter The First Number: "))
print("The list of operators that you can choose from: [+, -, /, * and %]")
operator = input("Enter the operator: ")
num2 = float(input("Enter The Second Number: "))

if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")

elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")

elif operator == "/":
    print(f"{num1} / {num2} = {num1 / num2}")

elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")

elif operator == "%":
    print(f"{num1} % {num2} = {num1 % num2}")

else:
    print("You have entered an invalid number or operator!")
