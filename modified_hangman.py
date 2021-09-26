import time, sys
import turtle
import emoji
from termcolor import colored as cl
import random
from colorama import Fore, Back, Style, init
from pyfiglet import Figlet

# instance the modules to use
# my_pen = turtle.Turtle()
init()
# define constants

GUEST_WORDS = []
SCORES = 0
TRIALS = 0

# set the data and variable the game game will be based on


words_to_guess = ["prison break", "game of thrones", "film", "vikings", "Rome", "person of interest",
                  "The scorpion", "pharmacy", "jkuat", "jecko", "pafiquinka", "hang"]


# invite people to game


def gameMenu():
    """
    This function retuns the available menus for the
    game.
    This menus can be selected based on the users desire
    :return:
    """
    option1 = "1. Proceed"
    option2 = "2. Cancel"
    option3 = "3. Help"
    option4 = "4. Quit"
    options = [option1, option2, option3, option4]
    for x in options:
        time.sleep(0.2)
        print(f"{'':30s}" + cl(f" {x} ", 'blue'))
        time.sleep(1.5)
    entry = input(f"\n{'':40s}" + cl(" [+] ", 'magenta', attrs=['dark']) + " ENTER SELECTION "
                + cl(" [+] ", 'magenta', attrs=['dark']) + ": ")
    try:
        if entry == '1':
            sys.stdout.flush()
            time.sleep(1)
            f = Figlet(font="standard")
            print(cl(f.renderText(f"{'':20s}!^Hangman^^!"), 'red'))
            time.sleep(2)
            play_game()
        elif entry == "2":
            print(cl(f"{'':40s}Hi! You canceled the game!"))
            sys.exit(0)
        elif entry == "3":
            time.sleep(0.2)
            print(cl(f"""{'':40s}
            This game involves quessing in which you have to 
            guess a word and feed in the word letter by letter
            The computer will make comparison between the entered letter 
            and the stored word and check if the letter exist in any of the words
            if so you'll be given a chance to proceed guessing
            If the word does not exist the the computer will print alert you and 
            then the remaining chances will also be reduced
            
            If you fail to get it correctly then the computer will shw you the 
            actual word
            The words are chosen based on the letters you chose
            """, 'green'))
            gameMenu()
        elif entry == "4":
            sys.exit(0)
    except ValueError as er:
        print(er.with_traceback)
        gameMenu()


def mainFunctionInvite():
    print(cl(f"\n{'':35s}[+]", "blue") + cl(" HANGMAN GAME CREATED BY PAFIQUINKA ", 'red') + cl(" [+]", "blue"), "\n")
    try:
        PLAYER_NAME = str(input(cl(f"{'':45s}Enter your name: ", "green")).capitalize())
    except ValueError:
        raise ValueError(cl("PLEASE ENTER NAME!", 'red'))
    print(f"{'':35s}[+] " + cl(f"{'':1s}Hi, {PLAYER_NAME}! Welcome to Hangman!.", 'white') + f"{'':4s}[+]")
    time.sleep(2)
    print(f"\n{'':29s} " + cl("****** ", 'red') + cl(" The Game is almost starting! Lets Play....", 'green') +
          cl(" ******", 'red'))
    print(f"{'':20s} " + cl("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", 'cyan'))
    print(f"\n{'':53s} " + cl("GAME MENU", 'magenta', attrs=['underline', 'blink']))
    time.sleep(1.5)
    gameMenu()


# define now variable that will be needed in
# in the running of the game


def play_game():
    global SCORES
    turns = 6
    guesses = ''
    wrong_guess = []
    # this list hold the already chosen letter so that we don't continue looping repeatedly
    already_selected = []
    word = random.choice(words_to_guess)
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                # we append the char
                already_selected.append(char)
                print(f"{''.join(char)}", end='')
            else:
                failed += 1
                continue
        if failed == 0:
            # tell the user he/she won
            # also return the right word
            print(f"{'':45} " + cl("[+]", 'blue') + cl(" CONGRATULATIONS ", 'green', attrs=['blink'])
                  + cl("[+]!", 'blue'))
            # let each letter in the word be a point
            # the longer the word the
            # more points the player gets instead of just adding the
            # fixed value to the scores value
            # that's explain why we use the len function and pass in the word
            SCORES += len(word)
            time.sleep(1)
            # now grate padding to the print out on the terminal
            print(f"\n{'':30} The word is" + cl(f"[{word.upper()}]!", 'yellow', attrs=['underline']) +
                  f"{'':20s} SCORES :[{SCORES:>20d}]")
            # the emoji is used here to print an emoji
            # congratulating the player
            print(f"\n{'':40s}" + cl(emoji.demojize(":thumbs_up:"), "magenta") * 3)
            time.sleep(2)
            # once the player has gained the points
            # we call the menu function again to allow him/her continue the game or quit
            gameMenu()
            break
        guess = input(f"\n{'':30s}" + cl("Letter Guess: ", 'blue'))
        guesses += guess
        wrong_guess.append(guess)
        if guess in already_selected:
            print(f"{'':40s}" + cl(f"YOU HAVE ALREADY SELECTED {guess}", 'yellow'))
            turns -= 1
            SCORES = SCORES
            guess = input(f"\n{'':30s}" + cl("Letter Guess: ", 'blue'))
            guesses += guess
            wrong_guess.append(guess)
        if guess not in word:

            turns -= 1

            # i use fidget to create a 3d image on the terminal
            # i intent to draw shape #
            f = Figlet(font='starwars')
            print(f"\n{'':40s} [!-!]" + cl(" Wrong guess!", 'red') + f"{'':2s}[!-!]")
            print(f"\n{'':38s}" + cl(f" [-]{cl(f.renderText(''), 'blue')} ", 'red',
                                     attrs=['dark']) + f"YOU HAVE  {turns} TURNS(s) LEFT" + cl("!", 'red'))
            if turns == 0:
                print(f"{'':39s} OUPS! YOU LOSS ! SCORES = {SCORES} \n{'':39s} RIGHT-WORD: " +
                      cl(f"{word.upper()}", "red")
                      + f" \n{'':39s} YOUR SELECTION: " + cl(f"{''.join([x for x in wrong_guess])}", 'red'))
                for word in words_to_guess:
                    print(f"{'':39s} The words to be selected are!")
                return word[:]


mainFunctionInvite()
