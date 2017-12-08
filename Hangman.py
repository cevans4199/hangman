import os
import random

def show_start():
    ("   _   _                                                                                                                                                   ")
    ("  | | | |                                                                                                                                                  ")
    ("  | |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __                                                                                                            ")
    ("  |  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \                                                                                                           ")
    ("  | | | | (_| | | | | (_| | | | | | | (_| | | | |                                                                                                          ")
    ("  \_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|                                                                                                          ")
    ("                      __/ |                                                                                                                                ")
    ("                     |___/                                                                                                                                 ")
    ("   _____                                            _           _   _             _____                  _                      _____                      ")
    ("  |  __ \                                          | |         | | | |           /  __ \                | |                    |  ___|                     ")
    ("  | |  \/ __ _ _ __ ___   ___    ___ _ __ ___  __ _| |_ ___  __| | | |__  _   _  | /  \/ ___  _   _ _ __| |_ _ __   ___ _   _  | |____   ____ _ _ __  ___  ")
    ("  | | __ / _` | '_ ` _ \ / _ \  / __| '__/ _ \/ _` | __/ _ \/ _` | | '_ \| | | | | |    / _ \| | | | '__| __| '_ \ / _ | | | | |  __\ \ / / _` | '_ \/ __| ")
    ("  | |_\ | (_| | | | | | |  __/ | (__| | |  __| (_| | ||  __| (_| | | |_) | |_| | | \__/| (_) | |_| | |  | |_| | | |  __| |_| | | |___\ V | (_| | | | \__ \ ")
    ("   \____/\__,_|_| |_| |_|\___|  \___|_|  \___|\__,_|\__\___|\__,_| |_.__/ \__, |  \____/\___/ \__,_|_|   \__|_| |_|\___|\__, | \____/ \_/ \__,_|_| |_|___/ ")
    ("                                                                           __/ |                                         __/ |                             ")

def get_name():
    name= input ("What is your name?")
    print ("Awesome, lets get started :)" + str(name))
    return name

def show_credits():
    print("This is the Hangman Game, by Courtney Evans.")
    print("$!$!$!$!$!$!$!$!$!$!$!$!$!$!$!$!$!$!$!$!$!$")


def get_puzzle():

path = "data"

file_names = os.listdir(path)

for i, f in enumerate(file_names):
    print(str(i)+ ")" + f)

choice = input ('pick one')
choice = int(choice)

file= path + "/" + file_names[choice]
print(file)

with open(file, 'r') as f:
    lines = f.read().splitlines()

print(lines)

category_name = lines[0]
puzzle = random.choice ( lines[1:])

print(category_name)
return puzzle

def get_solved (puzzle,guesses):
    solved= ""
    
    for letter in puzzle:
        if letter in guesses:
            solved += letter
        elif letter== " ":
            solved += " "
        else:
            solved += "-"

    return solved

def get_guess():
    letter = input("Guess a Letter" + str (name)+" ")
    

    if len(letter)== 1:
        return letter
    
    else:
        print("I do not understand" + str(name) + "." + " Enter a letter for your guess.")


def display_board(solved, strikes, true_guess, wrong_guess):
     print(solved)
     print("Strikes: " + str(strikes))
     print("True guesses: " + str(true_guess))
     print("False guesses: " + str(wrong_guess))

     
def show_results(strikes,limit,name):
    if strikes < limit:
        print("Congratulations! "  + str(name))
    else:
        print("Sorry, but that is incorrect" + str (name))
             
    
            
def play(name):

    puzzle = get_puzzle()
    guesses = ""
    true_guess = ""
    wrong_guess = ""
    solved = get_solved(puzzle, guesses)
    limit = 7
    strikes = 0

    print("You have" + str(limit) + "tries.")
    print(solved)

    while solved != puzzle and strikes < limit :
        letter = get_guess()

        if letter not in puzzle:
            strikes += 1
            wrong_guess += letter
        else:
            true_guess += letter


def play_again():
    while True:
        decision= input("Would you like to play again? (y/n)")
        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print ("I do not understand, please enter 'y' or 'n'.")

            
# Game starts running here

show_start()
name= get_name()

playing = True

while playing:
    play(name)
    playing= play_again()

show_credits()
    

