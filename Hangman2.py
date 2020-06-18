<<<<<<< HEAD
# Test
import random


def greeting():
    print('\n' * 50)
    print("Welcome to our Hangman game!\nYou will be playing against a computer.\n\n")


def dic_choice():
    try:
        choice = int(input(
            "Would you like to play\n 1. Locations\n 2. Movies\n 3. Video Games\n 4. Famous Companies\n\nType 1  2  3  "
            "4: "))

    except:
        print('Sorry please type a number from 1 to 4')

    else:
        return choice

def hangman_gui(guesses):
    if (guesses == 0):
	    print ("_________")
		print ("|	 |")
		print ("|")
		print ("|")
		print ("|")
		print ("|")
		print ("|________")
	elif (guesses == 1):
		print ("_________")
	    print ("|	 |")
		print ("|	 O")
		print ("|")
		print ("|")
		print ("|")
		print ("|________")
	elif (guesses == 2):
		print ("_________")
		print ("|	 |")
		print ("|	 O")
		print ("|	 |")
		print ("|	 |")
		print ("|")
		print ("|________")
	elif (guesses == 3):
		print ("_________")
		print ("|	 |")
		print ("|	 O")
		print ("|	\|")
		print ("|	 |")
		print ("|")
		print ("|________")
	elif (guesses == 4):
		print ("_________")
		print ("|	 |")
		print ("|	 O")
		print ("|	\|/")
		print ("|	 |")
		print ("|")
		print ("|________")
	elif (guesses == 5):
		print ("_________")
		print ("|	 |")
		print ("|	 O")
		print ("|	\|/")
		print ("|	 |")
		print ("|	/ ")
		print ("|________")
	elif (guesses == 6):
		print ("_________")
		print ("|	 |")
		print ("|	 O")
		print ("|	\|/")
		print ("|	 |")
		print ("|	/ \ ")
		print ("|________")
def print_dashes(word, list_word, guessed_letter, missed_let):
    if guessed_letter.lower() not in word and guessed_letter.upper() not in word:
        missed_let.append(guessed_letter)
        print(' '.join(list_word))
        return

    for num_char, char in enumerate(word):
        if char == guessed_letter.lower() or char == guessed_letter.upper():
            print("GOOD GUESS")
            list_word[num_char] = char

    print(' '.join(list_word))


def guessed_word(list_word, word):
    list_of_word = list(word)

    if list_of_word == list_word:
        return True

    return False


def len_word(word):
    word_len = 0

    for letter in word:
        if letter.isalpha():
            word_len += 1

        elif letter == ' ':
            continue

    return word_len


def guess_str(n):
    print(f'\n\nGuess a letter! It has {n} letters')


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
    guessed_let = ''

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

        while True:

            print('\n')
            print_dashes(word, list_word, guessed_let, missed_letters)
            num_char = len_word(word)

            word_guess = guessed_word(list_word, word)

            if word_guess:
                print('\nYou guessed the word!')
                game_yes = game_replay()

                if game_yes:
                    print('Lets play again!')

                    missed_letters = []
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

                    list_word = []
                    for chr in word:
                        if chr == ' ':
                            list_word.append(' ')
                            continue
                        list_word.append('_')
                    continue

                else:
                    print('Thank You for playing!')
                    return

            if len(missed_letters) != 0:
                print('\n')
                print('Wrong letters guessed: ')

                if len(missed_letters) > 6:
                    print('Sorry you lost. ')
                    game_yes = game_replay()

                    if game_yes:
                        print('Lets play again!')
                        continue

                    else:
                        print('Thank You for playing!')
                        return

                for character in missed_letters:
                    print(character + ' ', sep=' ', end='', flush=True)
            guesses = len(missed_letters)
            hangman_gui(guesses)
            guess_str(num_char)
            guessed_let = guess_letter()


if __name__ == "__main__":
    main()
=======
# Test
import random


def greeting():
    print('\n' * 50)
    print("Welcome to our Hangman game!\nYou will be playing against a computer.\n\n")


def dic_choice():
    try:
        choice = int(input(
            "Would you like to play\n 1. Locations\n 2. Movies\n 3. Video Games\n 4. Famous Companies\n\nType 1  2  3  "
            "4: "))

    except:
        print('Sorry please type a number from 1 to 4')

    else:
        return choice


def print_dashes(word, list_word, guessed_letter, missed_let):
    if guessed_letter.lower() not in word and guessed_letter.upper() not in word:
        missed_let.append(guessed_letter)
        print(' '.join(list_word))
        return

    for num_char, char in enumerate(word):
        if char == guessed_letter.lower() or char == guessed_letter.upper():
            print("GOOD GUESS")
            list_word[num_char] = char

    print(' '.join(list_word))


def guessed_word(list_word, word):
    list_of_word = list(word)

    if list_of_word == list_word:
        return True

    return False


def len_word(word):
    word_len = 0

    for letter in word:
        if letter.isalpha():
            word_len += 1

        elif letter == ' ':
            continue

    return word_len


def guess_str(n):
    print(f'\n\nGuess a letter! It has {n} letters')


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
    guessed_let = ''

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

        while True:

            print('\n')
            print_dashes(word, list_word, guessed_let, missed_letters)
            num_char = len_word(word)

            word_guess = guessed_word(list_word, word)

            if word_guess:
                print('\nYou guessed the word!')
                game_yes = game_replay()

                if game_yes:
                    print('Lets play again!')

                    missed_letters = []
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

                    list_word = []
                    for chr in word:
                        if chr == ' ':
                            list_word.append(' ')
                            continue
                        list_word.append('_')
                    continue

                else:
                    print('Thank You for playing!')
                    return

            if len(missed_letters) != 0:
                print('\n')
                print('Wrong letters guessed: ')

                if len(missed_letters) > 6:
                    print('Sorry you lost. ')
                    game_yes = game_replay()

                    if game_yes:
                        print('Lets play again!')
                        continue

                    else:
                        print('Thank You for playing!')
                        return

                for character in missed_letters:
                    print(character + ' ', sep=' ', end='', flush=True)

            guess_str(num_char)
            guessed_let = guess_letter()


if __name__ == "__main__":
    main()
>>>>>>> 2f21170d0d549ec535cbf2c3ca541873313d037a
