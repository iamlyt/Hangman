import random
import string

print('H A N G M A N')

win_count = 0
lost_count = 0

while True:

    player_input = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')

    list_of_player_inputs = ['play', 'results', 'exit']

    if player_input in list_of_player_inputs:
        if player_input == "results":
            print(f"You won: {win_count} times.\nYou lost: {lost_count} times.")
        elif player_input == "exit":
            break
        elif player_input == "play":
            list_of_words = ['python', 'java', 'swift', 'javascript']
            random_word = random.choice(list_of_words)

            print("\n" + "-" * len(random_word))

            # create an empty list to store letters inputted
            letters_inputted = []

            # store word into a list
            guessed_word = [*'-' * len(random_word)]

            alphabet_list = list(string.ascii_lowercase)

            attempts = 8

            while attempts > 0 and "-" in guessed_word:
                letter = input("Input a letter: ")

                # checks if letter is in English alphabet + if single letter + lowercase
                if letter not in alphabet_list:
                    if len(letter) != 1:
                        print("Please, input a single letter.")
                    else:
                        print("Please, enter a lowercase letter from the English alphabet.")
                    print('\n' + ''.join(guessed_word))
                    continue

                # checks if letter is repeated
                if letter in letters_inputted:
                    print("You've already guessed this letter.")
                    print('\n' + ''.join(guessed_word))
                    continue

                letters_inputted.append(letter)

                # checks if letter appears in word
                if letter not in random_word:
                    attempts -= 1
                    print("That letter doesn't appear in the word.")
                    # print(''.join(guessed_word))
                else:
                    for j in range(len(random_word)):
                        if random_word[j] == letter:
                            guessed_word[j] = letter

                if "-" in guessed_word:
                    print('\n' + ''.join(guessed_word))

            if "-" not in guessed_word:
                win_count += 1
                print(f"\nYou guessed the word {random_word}!\nYou survived!")
            else:
                lost_count += 1
                print("You lost!")

    else:
        continue
