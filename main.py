import random
import string

print("H A N G M A N\n")

list_of_words = 'python', 'java', 'swift', 'javascript'

random_word = random.choice(list_of_words)

print("-" * len(random_word))

# create an empty list to store letters inputted
letters_inputted = []

# store word into a list
guessed_word = [*'-' * len(random_word)]

alphabet_list = list(string.ascii_lowercase)

attempts = 8
count = 0

guess_str = "You've already guessed this letter."

while True:
    letter = input("Input a letter: ")

    # one letter + lowercase + only exist in English alphabet
    if len(letter) != 1 and letter not in alphabet_list:
        print("Please input a single letter.")

    elif letter.isupper() or letter not in alphabet_list:
        print("Please enter a lowercase letter from the English alphabet.")

    else:
        letters_inputted.append(letter)


    # delete this line after
    print("\nletters inputted: " + str(letters_inputted) + "\n")


    # if letter is not in word and if letter was suggested before
    if letter not in random_word:

        if letter not in letters_inputted:
            attempts -= 1
            print("That letter doesn't appear in the word.\n")
        elif letter in letters_inputted and letters_inputted.count(letter) > 1:
            print(guess_str)

    elif letter in guessed_word and letter in letters_inputted:
        print(guess_str)
    else:
        attempts -= 1
        for j in range(len(random_word)):
            if random_word[j] == letter:
                guessed_word[j] = letter


    print("attempt: " + str(attempts))

    print(''.join(guessed_word))

    if attempts == 0:
        if "-" in guessed_word:
            print("You lost!")
        else:
            print(f"You guessed the word {guessed_word}!\nYou survived!")
        break


