import random
import os
import re

# A program to play Rock, Paper, Scissors.
# Clear the console
os.system('cls' if os.name == 'nt' else 'clear')

i = 1
while i <= 5:
    print("\n")
    print("Rock, Paper, Scissors - Shoot!")

    # The users' input
    userChoice = input("Choose your weapon: Rock, Paper, or Scissors: ")
    # Helps to look for a similar pattern and returns the first occurrence
    if not re.match("[SsRrPp]", userChoice):
        print("Please choose a letter: ")
        print("Rock, Paper, Scissors - Shoot!")
        continue
    print(f"You chose: {userChoice}")

    choices = ['R', 'P', 'S']
    # The programs' random input
    opponentChoice = random.choice(choices)
    print(f"I chose: {opponentChoice}")

    # Conditions to winning or losing
    if opponentChoice == str.upper(userChoice):
        print("Tie!!!")
    elif opponentChoice == 'R' and userChoice.upper() == 'S':
        print("Scissors beats rock, I win!")
        continue
    elif opponentChoice == 'S' and userChoice.upper() == 'P':
        print("Scissors beats paper! I win!")
        continue
    elif opponentChoice == 'P' and userChoice.upper() == 'R':
        print("Paper beat rock, I win!")
        continue
    else:
        print("You win!")
    i += 1
