import random
import re
import sys
from simple_term_menu import TerminalMenu


print("Welcome to the Number Guessing Game!")
play_again = "yes"

while play_again == "yes":
    # show difficulty option menu
    difficulty_options = ["Easy (10 chances)", "Medium (5 chances)","Hard (3 chances)"]
    print("Please select the difficulty level:")
    terminal_menu = TerminalMenu(difficulty_options)
    menu_difficulty_index = terminal_menu.show()
    difficulty = difficulty_options[menu_difficulty_index]

    print("-"*25)
    chances = re.findall(r'\d+', difficulty) # extract all digits within a string
    chances = int(chances[0])
    difficulty = re.match(r'^[^(]*', difficulty).group() # extract every character till you encounter '('
    print(f"Great! You have selected the {difficulty}difficulty level")
    print("-"*25)
    print(f"You have {chances} chances to guess the correct number")
    print("I'm thinking of a number between 1 and 100")
    print("Let's start the game!")

    pc_number = random.randint(1,100)
    guess = 0
    attempt = 0

    while attempt != chances:
        # validating user input
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice <= 0 or choice > 100:
                    print("Invalid input! Please enter a number between 1 and 100.")
                    continue
            except (ValueError, NameError):
                print("Invalid input! Please enter a number between 1 and 100.")
                continue
            except Exception as e:
                print(f"Encounted an unexpected error: {e}\nExiting...")
                sys.exit()
            break

        attempt += 1

        if choice > pc_number:
            print(f"Incorrect! The number is less than {choice}.")
        elif choice < pc_number:
            print(f"Incorrect! The number is greater than {choice}.")
        else:
            break

    if choice == pc_number:
        print(f"Congratulations! You guessed the correct number in {attempt} attempts.")
    else:
        print(f"Game Over! You've run out of chances! The correct number was: {pc_number}")

    # show restart option menu
    restart_options = ["yes", "no"]
    print("-"*25)
    print("Do you want to play again?")
    print("-"*25)
    menu_restart_index = TerminalMenu(restart_options).show()
    play_again = restart_options[menu_restart_index]

print("-"*25)
print("Thank you for playing! See you soon!")