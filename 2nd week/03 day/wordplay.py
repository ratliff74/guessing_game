import random


def show_instructions():
    print("""You have 7 chances to guess the correct letter from the secret word.
After 7 incorrect guesses, the game will end. """)
    print('='*60)


def random_word():
    my_list = ["apple", 'banana', 'watermelon', 'strawberry',
               'blueberry', 'pear', 'kiwi', 'grapes', 'blackberry', 'mango']
    secret_word = list(random.choice(my_list))
    word_to_guess = ['_' for letter in secret_word]
    print(" ".join(word_to_guess))
    return(secret_word)


def wordplay():

    show_instructions()
    secret_word = random_word()

    guesses_left = 7
    while guesses_left > 0:
        decision = input("pick a letter: ").lower()
        if decision not in secret_word:
            guesses_left -= 1
            print("you have this many guesses left:", + guesses_left)

        elif decision in secret_word:
            #all characters from the input
            #secret_word taking one at a time

            for character in secret_word:
                if character in secret_word:
                    print(character, end=" ")
            print("nice!")
#         print(secret_word)


wordplay()
