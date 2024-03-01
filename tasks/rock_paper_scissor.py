# Program: Rock Paper Scissors Game
# 
# Description: Asking a user to enter their name and choice from the given options to play with a computer
#
# Author: DHLAMINI SNYMAN @ https://www.github.com/SnymanD

import random

print("Rock Paper Scissors Game")
print("-------------------------")
print("")

options = ("rock", "paper", "scissors")
name = input("Enter Your Name: ").capitalize()
print("")


def play():
    
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input(f"Enter a choice {name} (rock, paper, scissors): ").lower()
        print("")

    print(f"{name}: {player}")
    print(f"Computer: {computer}")
    print("")

    if player == computer:
        print("It's a tie! \n")
        
    elif player == "rock" and computer == "scissors":
        print("You win! \n")
        
    elif player == "paper" and computer == "rock":
        print("You win! \n")
        
    elif player == "scissors" and computer == "paper":
        print("You win! \n")
        
    else:
        print("You lose! \n")
        

while True:
    
    choose = int(input(f"{1}. Play Game \n"
                       f"{2}. Quit \n"
                       ">>> Choose 1 or 2: "))
    print("")
    
    if choose == 1:
        play()
    
    elif choose == 2:
        print(f"Thanks for playing {name}!")
        print("")
        break
