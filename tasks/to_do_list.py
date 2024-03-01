# Program: To Do List Application
# 
# Description: This project aims to create a command-line or GUI-based application using Python, allowing
#              users to create, update, and track their to-do lists
#
# Author: DHLAMINI SNYMAN @ https://www.github.com/SnymanD

tasks = []


# A function for listing all the tasks in the to-do-list
def track_tasks():
    if not tasks:
        print("____Currently you do not have any tasks____")
    else:
        print("________Current Tasks________")
        for index, task in enumerate(tasks):
            print(f"{index}. {task}")


# Function for adding new tasks
def create_tasks():
    task = input("Please Enter A New Task: ").capitalize()
    tasks.append(task)
    print(f"'{task}' is added on your list.")


# Function to delete tasks
def remove_tasks():
    track_tasks()

    task_to_remove = int(input("Enter the number of the task to delete: "))
    if 0 <= task_to_remove < len(tasks):
        tasks.pop(task_to_remove)
        print("The task has been deleted.")
        track_tasks()
    else:
        print(f"{task_to_remove} was not found.")


if __name__ == "__main__":

    print("Welcome to To-Do-List app")
    print("--------------------------")
    while True:
        print("")
        print("Select One Of The Following Options: ")
        print(f"{1}. List all the tasks")
        print(f"{2}. Add a new task")
        print(f"{3}. Delete a task")
        print(f"{4}. Quit")

        choice = int(input("Select a number: "))

        if choice == 1:
            track_tasks()
        elif choice == 2:
            create_tasks()
        elif choice == 3:
            remove_tasks()
        elif choice == 4:
            break
        
print("Bye!")