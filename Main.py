# Test
import time
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


def print_dashes(dictionary, location, movie, video_game, famous_company):
    rand_int = random.randrange(0, 5)

    if dictionary == 1:
        for char in location[rand_int]:
            if char == ' ':
                print(' ', sep=' ', end='', flush=True)

            else:
                print('_ ', sep=' ', end='', flush=True)

        return len(location[rand_int])

    if dictionary == 2:
        for char in movie[rand_int]:
            if char == ' ':
                print(' ', sep=' ', end='', flush=True)

            else:
                print('_ ', sep=' ', end='', flush=True)

        return len(movie[rand_int])

    if dictionary == 3:
        for char in video_game[rand_int]:
            if char == ' ':
                print(' ', sep=' ', end='', flush=True)

            else:
                print('_ ', sep=' ', end='', flush=True)

        return len(video_game[rand_int])

    if dictionary == 4:
        for char in famous_company[rand_int]:
            if char == ' ':
                print(' ', sep=' ', end='', flush=True)

            else:
                print('_ ', sep=' ', end='', flush=True)

        return len(famous_company[rand_int])

def guess_str(n):
    print(f'Guess a letter! It has {n} letters')


def main():
    game_on = True
    locations = {"Paris": 5, "Brussels": 8, "London": 6, "Chicago": 7, "New York City": 11}
    movies = {"Matrix": 6, "Inception": 9, "Venom": 5, "Star Wars": 8, "The Godfather": 12}
    video_games = {"Fortnite": 7, "Warzone": 7, "FIFA": 4, "Minecraft": 9, "Pac Man": 6}
    famous_companies = {"Apple": 5, "Microsoft": 9, "Oracle": 6, "Nike": 4, "Tesla": 5}

    location_keys = list(locations.keys())
    movie_keys = list(movies.keys())
    video_game_keys = list(video_games.keys())
    famous_company_keys = list(famous_companies.keys())

    while game_on:
        chances = 6
        greeting()
        user_choice = dic_choice()
        print('\n')

        num_char = print_dashes(user_choice, location_keys, movie_keys, video_game_keys, famous_company_keys)
        print('\n')
        guess_str(num_char)
        while chances > 0:
            pass


if __name__ == "__main__":
    main()
