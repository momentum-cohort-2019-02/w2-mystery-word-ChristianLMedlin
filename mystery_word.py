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








#imports, reads, and splits each item from words.txt into seperate words and saves them into my_words as a list.

my_words = open('words.txt', "r").read().split()


#Declares the lists for use in the following function.

easy_list = []
normal_list = []
hard_list = []


#Checks the length of each item and moves them into appropriate lists.

# for w in my_words:
#     if len(w) in range(8, 99):
#         hard_list.append(w)
#     elif len(w) in range(4, 9):
#         if len(w) in range (4, 7) and len(w) not in range(7, 9):
#             easy_list.append(w)
#             if len(w) in range (6, 9):
#                 normal_list.append(w)
#         else: 
#             normal_list.append(w)

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




