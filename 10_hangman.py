from words import words
import random
import string


def select_valid_word(words):
    word_selected = random.choice(words)
    while ('-' in word_selected) or (' ' in word_selected):
        word_selected = random.choice(words)

    return word_selected.upper()


def hangman():

    list_of_alphabets = []
    list_of_alphabets = string.ascii_uppercase

    hangman_word = select_valid_word(words)

    used_letters = []  # List of letters alredy inputted by the user

    # set of letters in the selected word
    list_of_letters_in_word = set(hangman_word)

    # number of lives

    lives = 10
    # We use set to store the list of alphabets in the word because:
    # The major difference is that sets, unlike lists or tuples, cannot have multiple occurrences of the same element and store unordered values.

    while(len(list_of_letters_in_word) > 0) and lives > 0:
        print('You have used the following letters : ', ' '.join(used_letters))

        print(f"You have {lives} number of lives left ")

        # print what the current word is hangman style [ example ->  W - O R D - D]
        word_list = []
        for letter in hangman_word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append('-')
        print('Current word : ', ' '.join(word_list))

        user_input = input("Guess a letter : ").upper()
        if(user_input in used_letters):
            print("Already guessed that letter ")
        elif(user_input not in list_of_alphabets):
            print("Please enter valid characted ")
        else:
            used_letters.append(user_input)
            if(user_input in list_of_letters_in_word):
                list_of_letters_in_word.remove(user_input)
            elif(user_input not in list_of_letters_in_word):
                lives -= 1
    # gets here when len(list_of_letters_in_word == 0 ) or lives have ended
    if(lives > 0):
        print(f"You have correctly guessed the word : {hangman_word} ")

    else:
        print("Game over, you ran out of lives :( ")
        print(f"The word was {hangman_word}")


hangman()
