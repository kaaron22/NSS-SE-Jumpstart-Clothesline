import random

def main():

    clear_screen()
    
    # counter for number of incorrect guesses
    incorrect_guess_count = 0

    # random letter that, if guessed, will award the player an extra guess (only once per game)
    # bonus_guess_letter = "a" # used for testing function
    bonus_guess_letter = chr(random.randint(ord("a"), ord("z")))

    # flag to indicate whether player still eligible to earn the extra guess (set to false after guessing the bonus letter)
    bonus_guess_eligible = True

    # flag to indicate whether bonus guess message has already been printed (set to True after printing)
    bonus_message_printed = False

    # list of letters guessed thus far for display/reminder to player
    # letters_guessed = [] # list format was not ideal for printout
    letters_guessed = ""

    # Welcome player and prompt for word option selection (i.e. easy words, animals, etc.)
    word_category_selection = welcome_options()

    # randomly set the secret word based on word category selected by player
    secret_word = pick_secret_word(word_category_selection)

    # create appropriate number of dashes to display to player based on length of secret word
    secret_word_length = len(secret_word)
    guessed_word = "_" * secret_word_length

    # variable for determining what color the guesses are printed
    # 0 = normal, when no letters guessed
    # 1 = green, when last letter guess is correct
    # 2 = red, when last letter guess is incorrect
    letter_guess_color_code = 0

    # our main loop for playing the game - guessing letters and updating the display
    while incorrect_guess_count < 8 and guessed_word != secret_word:
        
        # declaration to ensure player does not enter nothing
        letter_to_check = ""

        # continue asking player for a letter guess
        while letter_to_check == "":
            clear_screen()

            # message indicating that bonus has been added
            if bonus_guess_eligible == False and bonus_message_printed == False:
                print_green("BONUS GUESS ADDED!")
                bonus_message_printed = True

            # print display of shirts on the clothesline indicating the number of incorrect guesses remaining
            print_clothesline(incorrect_guess_count)

            # print the secret word with dashes for letters remaining to be guessed, as well as letters successfully guessed
            print_guessed_word(guessed_word)

            # print the word category for player's reference
            print_word_category(word_category_selection)

            # print the list of letters attempted so far, including both correct and incorrect
            print_guessed_letters(letters_guessed, letter_guess_color_code)
            
            # ask player to guess a letter
            print("Guess a letter...if you dare!")
            letter_to_check = input("> ")

        # add current letter guessed to list for display
        # letters_guessed.append(letter_to_check) # list version was not ideal for printout
        letters_guessed = letters_guessed + letter_to_check[0] # add only the first letter to list, if player enters more than single letter for guess
        letters_guessed = letters_guessed + " " # for separation between letters when displayed

        if letter_to_check == bonus_guess_letter and bonus_guess_eligible == True:
            print()
            print_green("You guessed the bonus letter! You've earned an additional guess! Please press Enter to continue.")
            input()
            bonus_guess_eligible = False
            incorrect_guess_count = incorrect_guess_count - 1

        # check secret word for presence of letter guessed (only the first letter, if player enters more than single letter for guess)
        letter_is_in_word = is_letter_in_word(letter_to_check[0], secret_word)
        if letter_is_in_word == True:
            # print("Correct!") # no longer need this message since we now have a visual indicator

            # update the display to include the successfully guessed letter
            guessed_word = update_guess(guessed_word, letter_to_check[0], secret_word)

            # update to print guesses in green
            letter_guess_color_code = 1
        else:
            # print("Incorrect!") # no longer need this message since we now have a visual indicator

            # update counter for clothesline art since the guess was incorrect
            incorrect_guess_count = incorrect_guess_count + 1

            # update to print guesses in red
            letter_guess_color_code = 2

    # final update of display after leaving the main loop

    clear_screen()

    # print display of shirts on the clothesline indicating the number of incorrect guesses remaining
    print_clothesline(incorrect_guess_count)
    
    # print the secret word with dashes for letters remaining to be guessed, as well as letters successfully guessed
    print_guessed_word(guessed_word)

    # print the word category for player's reference
    print_word_category(word_category_selection)

    # print the list of letters attempted, including both correct and incorrect
    print_guessed_letters(letters_guessed, letter_guess_color_code)

    # print the secret word now that the game is over, if not guessed correctly
    if guessed_word != secret_word:
        print("The secret word was: " + secret_word)
        print()

    # print a message indicating whether or not the player won
    if guessed_word == secret_word:
        print_green("YOU WON!")
    else:
        print_red("YOU LOST!")
    print()


def clear_screen():
    print("\033[H\033[J", end="")


def welcome_options():
    # Prompt player for preferred category of words
    word_category = ""
    while word_category != "easy" and word_category != "animals" and word_category != "fruits" and word_category != "hard" and word_category != "all":
        clear_screen()
        title_border = "*" * 65
        print(title_border)
        print("Welcome to Clothesline, your family-friendly version of H###-man!")
        print(title_border)
        print()
        word_category = input("Which category of words do you prefer? ('easy', 'animals', 'fruits', 'hard', or 'all') ")
    return word_category


def pick_secret_word(word_category):
    # read words into list according to player's selection and then select random word from the list 
    if word_category == "easy":
        f = open("easy_words.txt", encoding='utf-8')
        secret_word_options = f.read().splitlines()
        random_secret_word = random.choice(secret_word_options)
    elif word_category == "animals":
        f = open("animals.txt", encoding='utf-8')
        secret_word_options = f.read().splitlines()
        random_secret_word = random.choice(secret_word_options)
    elif word_category == "fruits":
        f = open("fruits.txt", encoding='utf-8')
        secret_word_options = f.read().splitlines()
        random_secret_word = random.choice(secret_word_options)
    elif word_category == "hard":
        f = open("hard_words.txt", encoding='utf-8')
        secret_word_options = f.read().splitlines()
        random_secret_word = random.choice(secret_word_options)
    else:
        f = open("easy_words.txt", encoding='utf-8')
        easy_words = f.read().splitlines()
        f = open("animals.txt", encoding='utf-8')
        animals = f.read().splitlines()
        f = open("fruits.txt", encoding='utf-8')
        fruits = f.read().splitlines()
        f = open("hard_words.txt", encoding='utf-8')
        hard_words = f.read().splitlines()
        secret_word_options = easy_words + animals + fruits + hard_words
        random_secret_word = random.choice(secret_word_options)

    f.close()

    # secret_word_options = ["apple", "pear", "banana", "grape", "scorpion", "umbrella", "watermelon"]
    
    return random_secret_word


def print_clothesline(wrong_guesses):
    if wrong_guesses == -1:
       print_green(r"""
=====!=====!=======!=====!=======!=====!=======!=====!=======!=====
    /'''V'''\     /'''V'''\     /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-' '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |       |     |       |     |      | B |
     |     |       |     |       |     |       |     |      |   |
     ```````       ```````       ```````       ```````      `-._|


""")

    elif wrong_guesses == 0:
        print_green(r"""
=====!=====!=======!=====!=======!=====!=======!=====!=============
    /'''V'''\     /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |       |     |
     |     |       |     |       |     |       |     |
     ```````       ```````       ```````       ```````


""")

    elif wrong_guesses == 1:
        print_green(r"""
=====!=====!=======!=====!=======!=====!=======!===================
    /'''V'''\     /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |       |     |      |   |
     |     |       |     |       |     |      |   |
     ```````       ```````       ```````      `-._|


""")

    elif wrong_guesses == 2:
        print_green(r"""
=====!=====!=======!=====!=======!=====!===========================
    /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |
     |     |       |     |       |     |
     ```````       ```````       ```````
                                            _.~.,_.._
                                             ```````
""")

    elif wrong_guesses == 3:
        print_yellow(r"""
=====!=====!=======!=====!=======!=================================
    /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |      |   |
     |     |       |     |      |   |
     ```````       ```````      `-._|
                                            _.~.,_.._
                                             ```````
""")

    elif wrong_guesses == 4:
        print_yellow(r"""
=====!=====!=======!=====!=========================================
    /'''V'''\     /'''V'''\
   /         \   /         \
  '-"|     |"-' '-"|     |"-'
     |     |       |     |
     |     |       |     |
     ```````       ```````
                              _.~.,_.._     _.~.,_.._
                               ```````       ```````
""")

    elif wrong_guesses == 5:
        print_yellow(r"""
=====!=====!=======!===============================================
    /'''V'''\     /'\
   /         \   /   .\
  '-"|     |"-'  '|  ='
     |     |      |   |
     |     |      |   |
     ```````      `-._|
                              _.~.,_.._     _.~.,_.._
                               ```````       ```````
""")

    elif wrong_guesses == 6:
        print_red(r"""
=====!=====!=======================================================
    /'''V'''\
   /         \
  '-"|     |"-'
     |     |
     |     |
     ```````
                _.~.,_.._     _.~.,_.._     _.~.,_.._
                 ```````       ```````       ```````
""")

    elif wrong_guesses == 7:
        print_red(r"""
=====!=============================================================
    /'\
   /   .\
   '|  ='
    |   |
    |   |
    `-._|
                _.~.,_.._     _.~.,_.._     _.~.,_.._
                 ```````       ```````       ```````
""")

    else:
        print_red(r"""
===================================================================






  _.~.,_.._     _.~.,_.._     _.~.,_.._     _.~.,_.._
   ```````       ```````       ```````       ```````
""")

    print()

    # displayed number of guessed remaining before we updated the code to indicate this by way of clothesline art
    # so this is no longer needed
    # guesses_remaining = 8 - wrong_guesses
    # str_guesses_remaining = str(guesses_remaining)
    # print("You have " + str_guesses_remaining + " guesses remaining!")


def print_guessed_word(guess_so_far):
    # print the secret word with dashes for letters remaining to be guessed, as well as letters successfully guessed
    print("Word:      " + guess_so_far)
    print()


def print_word_category(word_category):
    print("Category:  " + word_category)
    print()


def print_guessed_letters(letters_so_far, color):
    # print the list of letters attempted so far, including both correct and incorrect
    if color == 0: # print normal when no letters have been guessed
        print("Guesses: " + letters_so_far)
    elif color == 1: # print in green when last letter guessed was correct
        print("\033[0;32;40m" + "Guesses: " + "\033[0;0m" + letters_so_far)
    else: # print in red when last letter guessed was incorrect
        print("\033[0;31;40m" + "Guesses: " + "\033[0;0m" + letters_so_far)
    print()


def is_letter_in_word(letter, word):
    if letter in word:
        return True
    else:
        return False


def update_guess(old_guess, letter, secret_word):
    # new_guess string variable updated with correctly guessed letter(s) and remaining unguessed letters by method of concatenation
    new_guess = ""
    for index in range(len(secret_word)):
        # for each position of letter that was correctly guessed, it should now be displayed by changing it from a dash to the letter
        if letter == secret_word[index]:
            new_guess = new_guess + secret_word[index] # we could also add the 'letter' variable instead of using the secret_word[index] variable

        # for each letter that remains to be guessed, it still needs to be displayed as a dash
        else:
            new_guess = new_guess + old_guess[index] # we could also simply add "-" instead of using the old_guess variable
    return new_guess


def print_green(msg):
    print("\033[0;32;40m" + msg + "\033[0;0m")


def print_yellow(msg):
    print("\033[0;33;40m" + msg + "\033[0;0m")


def print_red(msg):
    print("\033[0;31;40m" + msg + "\033[0;0m")


main()