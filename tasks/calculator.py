# Design a simple calculator with basic arithmetic operations
# Prompt the user to input two numbers and an operation choice
# Perform the calculation and display the result

print("Calculator Application")
print("----------------------")

while True:
    print("Choose whether you want to use the calculator or quit: ")
    choice = int(input(f"{1}. Continue calculation \n"
                       f"{2}. Quit \n"
                       f">>> \n"))
    if choice == 1:
        num1 = float(input("Enter The First Number: "))
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
            print("You have entered an operator!")
    elif choice == 2:
        break
