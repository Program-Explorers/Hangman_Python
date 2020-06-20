import random


def greeting():
    print('\n' * 20)
    print("Welcome to our Hangman game!\nYou will be playing against a computer.\n\n")


def dic_choice():
    print('\n' * 20)
    try:
        choice = int(input(
            "Would you like to play\n 1. Locations\n 2. Movies\n 3. Video Games\n 4. Famous Companies\n\nType 1  2  3  "
            "4: "))

    except:
        print('Sorry please type a number from 1 to 4')

    else:
        return choice


def hangman_gui(guesses):
    print('\n' * 20)
    if guesses == 0:
        print("_________")
        print("|	 |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|________")

    elif guesses == 1:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|")
        print("|")
        print("|")
        print("|________")

    elif guesses == 2:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	 |")
        print("|	 |")
        print("|")
        print("|________")

    elif guesses == 3:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|")
        print("|	 |")
        print("|")
        print("|________")

    elif guesses == 4:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|")
        print("|________")

    elif guesses == 5:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|	/ ")
        print("|________")

    elif guesses == 6:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|	/ \ ")
        print("|________")


def print_dashes(word, list_word, guessed_letter, missed_let):
    for num_char, char in enumerate(word):
        if char == guessed_letter.lower() or char == guessed_letter.upper():
            list_word[num_char] = char
            print("GOOD GUESS")

    print(' '.join(list_word))
    return


def len_word(word):
    word_len = 0

    for letter in word:
        if letter.isalpha():
            word_len += 1

        elif letter == ' ':
            continue

    return word_len


def guess_str(n):
    print(f'\nGuess a letter! It has {n} letters')


def guess_letter():
    while True:
        letter = input('Type in a letter: ')
        letter = letter.lower()
        if letter.isalpha():
            return letter

        else:
            print('Sorry that is not a letter')
            continue


def game_replay():
    game_yes = input('Do you want to play again? (Y/N) ')

    if game_yes.lower() == 'y':
        return True

    else:
        return False


def did_win(user_word, real_word):
    if user_word == real_word:
        return True

    return False


def main():
    missed_letters = []
    game_on = True
    locations = {"Paris": 5, "Brussels": 8, "London": 6, "Chicago": 7, "New York City": 11}
    movies = {"Matrix": 6, "Inception": 9, "Venom": 5, "Star Wars": 8, "The Godfather": 12}
    video_games = {"Fortnite": 7, "Warzone": 7, "FIFA": 4, "Minecraft": 9, "Pac Man": 6}
    famous_companies = {"Apple": 5, "Microsoft": 9, "Oracle": 6, "Nike": 4, "Tesla": 5}

    location_keys = list(locations.keys())
    movie_keys = list(movies.keys())
    video_game_keys = list(video_games.keys())
    famous_company_keys = list(famous_companies.keys())
    guessed_let = ';'

    while game_on:

        rand_int = random.randrange(0, 5)

        greeting()
        user_choice = dic_choice()
        if user_choice == 1:
            word = location_keys[rand_int]

        elif user_choice == 2:
            word = movie_keys[rand_int]

        elif user_choice == 3:
            word = video_game_keys[rand_int]

        else:
            word = famous_company_keys[rand_int]

        list_word = []
        for chr in word:
            if chr == ' ':
                list_word.append(' ')
                continue
            list_word.append('_')

        list_of_word = list(word)  # a list of the characters of the word

        while True:
            num_char = len_word(word)  # gets length of the word without spaces

            hangman_gui(len(
                missed_letters))  # prints the hangman picture and returns true if the user has made more than 6 guesses
            print_dashes(word, list_word, guessed_let, missed_letters)
            num_of_wrong_guess = len(missed_letters)
            print('\nMissed letters: ' + ' '.join(missed_letters))
            did_user_win = did_win(list_of_word,
                                   list_word)  # sees if the dash words is equal to the original word and stores in var

            if did_user_win:

                print('\nYou GUESSED the word! Great job.')
                game_yes = game_replay()

                if game_yes:
                    print('Lets play again!')
                    guessed_let = ''
                    missed_letters = []
                    list_word = []

                    rand_int = random.randrange(0, 5)
                    user_choice = dic_choice()

                    if user_choice == 1:
                        word = location_keys[rand_int]

                    elif user_choice == 2:
                        word = movie_keys[rand_int]

                    elif user_choice == 3:
                        word = video_game_keys[rand_int]

                    else:
                        word = famous_company_keys[rand_int]

                    for char in word:
                        if char == ' ':
                            list_word.append(' ')

                        else:
                            list_word.append('_')

                    list_of_word = list(word)
                    continue

                else:
                    print('Thank you for playing')
                    return

            if num_of_wrong_guess == 6:

                print('Sorry you lost. ')
                game_yes = game_replay()

                if game_yes:
                    print('Lets play again!')
                    continue

                else:
                    print('Thank You for playing!')
                    return

            guess_str(num_char)
            guessed_let = guess_letter()

            if guessed_let.lower() not in word and guessed_let.upper() not in word and guessed_let != ';':
                missed_letters.append(guessed_let)

            for character in missed_letters:
                print(character + ' ', sep=' ', end='', flush=True)


if __name__ == "__main__":
    main()
