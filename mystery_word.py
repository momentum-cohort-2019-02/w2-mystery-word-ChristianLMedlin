# The game must be interactive; the flow of the game should go as follows:

# 1. Let the user choose a level of difficulty at the beginning of the program.
#    Easy mode only has words of 4-6 characters; normal mode only has words of 6-8
#    characters; hard mode only has words of 8+ characters.

# 2. At the start of the game, let the user know how many letters the computer's
#    word contains.

# 3. Ask the user to supply one guess (i.e. letter) per round. This letter can be
#    upper or lower case and it should not matter. If a user enters more than one
#    letter, tell them the input is invalid and let them try again.

# 4. Let the user know if their guess appears in the computer's word.

# 5. Display the partially guessed word, as well as letters that have not been
#    guessed. For example, if the word is BOMBARD and the letters guessed are a, b,
#    and d, the screen should display:

# ```
# B _ _ B A _ D
# ```

# A user is allowed 8 guesses. Remind the user of how many guesses they have left
# after each round.

# _A user loses a guess only when they guess incorrectly._ If they guess a letter
# that is in the computer's word, they do not lose a guess.

# If the user guesses the same letter twice, do not take away a guess. Instead,
# print a message letting them know they've already guessed that letter and ask
# them to try again.

# The game should end when the user constructs the full word or runs out of
# guesses. If the player runs out of guesses, reveal the word to the user when
# the game ends.

# When a game ends, ask the user if they want to play again. The game begins
# again if they reply positively.


import random




#imports, reads, and splits each item from words.txt into seperate words and saves them into my_words as a list.

my_words = open('words.txt', "r").read().split()


#Declares the lists for use in the following function.

easy_list = []
normal_list = []
hard_list = []


play_again = "y"


while play_again == "y":

    previous_guesses = []

    #Checks the length of each item and copies them into appropriate lists.
    for w in my_words:
        if len(w) == 8:
            hard_list.append(w)
            normal_list.append(w)
        elif len(w) in range (9, 99):
            hard_list.append(w)

        if len(w) == 6:
            normal_list.append(w)
            easy_list.append(w)
        elif len(w) in range (7, 8):
            normal_list.append(w)

        if len(w) == 4:
            easy_list.append(w)
        elif len(w) in range (4, 6):
            easy_list.append(w)


    #Defines the variable that will be used after the user selects the desired difficulty.

    computer_list = None
    user_letter = None


    #Asks the user for their difficulty input, allowing only the input Easy, Normal, or Hard.
    #If user_difficulty != easy, medium, or hard, asks again.

    user_difficulty = None

    while user_difficulty not in ['easy', 'normal', 'hard']:
        user_difficulty = input("\nEnter your difficult: Easy, Normal, or Hard. ").lower()
        if user_difficulty == 'easy':
            print("\n \n \n \n \n \n \n \n \n\n \n Beginning the game on Easy, Snowflake. \n \n \\(ᵔᵕᵔ)/ \n")
        elif user_difficulty == 'normal':
            print("\n \n \n \n \n \n \n \n \n\n \n Beginning the game on Normal. \n \n ಠ_ಠ \n")
        elif user_difficulty == 'hard':
            print("\n \n \n \n \n \n \n \n \n\n \n Beginning the game on Hard, Big Brain. \n \n (╯°□°)╯ ︵ ┻━┻ \n")
        else:
            print("\nYour difficulty must be either Easy, Normal, or Hard.\n")


    #Chooses the correct list based on the difficulty selected by user.

    if user_difficulty == 'easy':
        computer_list = easy_list
    elif user_difficulty == 'normal':
        computer_list = normal_list
    elif user_difficulty == 'hard':
        computer_list = hard_list


    #chooses a word randomly from the list using the Random library's method '.choice'. 
    mystery_word = random.choice(computer_list).lower()


    #Prints the length of the mystery word.
    print("The mystery word contains", len(mystery_word), "letters.\n")


    #Splits each character in mystery_word into a seperate list, then creates another list with blanks equal to the length of the mystery word.
    mystery_word = list(mystery_word)

    display_word = "_ " * len(mystery_word)


    #Displays the blank spaces to the user.
    print (display_word, "\n")


    #Removes the spaces from display_word.
    display_word = display_word.replace(" ", "")

    display_word = list(display_word)


    #Requests the number of turns the player wishes to have
    user_guesses = input("How many turns do you wish to have? \n")


    #Checks to see whether or not it is safe to convert user_guesses into an int.
    while user_guesses.isdigit() != True:
        try:
            user_guesses = int(user_guesses)
        except ValueError:
            user_guesses = input("Your number of turns must actually be, you know, a number. ")
            continue


    #converts user_guesses into an int.
    user_guesses = int(user_guesses)

    #checks whether or not user_letter is in the mystery word.
    def mystery_word_checker(amount_of_guesses):
        if "_" not in display_word:
            return (print("You win!\n"))
        if amount_of_guesses > 0:
            user_letter = input("Enter a single letter. \n \n").lower()

            #Checks whether or not user_letter is a single letter.
            while user_letter.isalpha() != True or len(user_letter) != 1:
                user_letter = input("You must select a single letter.\n").lower()
            if user_letter in previous_guesses:
                print("You've already that letter, choose a different letter!\n")
                mystery_word_checker(amount_of_guesses)
            else:    
                previous_guesses.append(user_letter)
                #If the user_letter is in mystery_word, attempts to replace that index in display_word
                if user_letter in mystery_word:
                    #Iterates through mystery_word until all appropriate letters are replaced. This actually took like 5 hours to figure out, holy shit.

                    for x in range(0, len(mystery_word)):
                        if mystery_word[x] == user_letter:
                            display_word[x] = user_letter
                    print(display_word)
                    mystery_word_checker(amount_of_guesses)  
                else:
                    amount_of_guesses -= 1
                    print("The letter", user_letter, "is not in the mystery word.\n You have", amount_of_guesses, "remaining.\n")
                    print (display_word, "\n")
                    mystery_word_checker(amount_of_guesses)
        else:
            reveal_word = "".join(mystery_word)
            return(print('Game over.\n The word was', reveal_word), "\n")




    mystery_word_checker(user_guesses)

    play_again = input('Would you like to play again? Y / N \n').lower()

    while play_again != 'y' and play_again != "n":
        play_again = input('Would you like to play again? Y / N\n').lower()


else: 
    print("See you, space cowboy.\n")


#######   Play_again does not work properly.