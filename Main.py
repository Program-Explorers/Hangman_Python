#Test
import time
import random

def greeting():
    print('\n'*50)
    print("Welcome to our Hangman game!\nYou will be playing against a computer.\n\n")

def dic_choice():
    try:
        choice = int(input("Would you like to play\n 1. Locations\n 2. Movies\n 3. Video Games\n 4.Famous Companies\n\nType 1  2  3  4: "))
        
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
def main():
    game_on = True
    locations = {"Paris": 5, "Brussels": 8, "London": 6, "Chicago": 7, "New York City": 11}
    movies = {"Matrix": 6, "Inception": 9, "Venom": 5, "Star Wars": 8, "The Godfather": 12}
    video_games = {"Fornite": 7, "Warzone": 7, "FIFA": 4, "Minecraft": 9, "Pac Man": 6}
    famous_companies = {"Apple": 5, "Microsoft": 9, "Oracle": 6, "Nike": 4, "Tesla": 5}
    
    location_keys = list(locations.keys())
    movie_keys = list(movies.keys())
    video_game_keys = list(video_games.keys())
    famous_companie_keys = list(famous_companies.keys())
    
    while game_on:
        chances = 6
        greeting()
        user_choice = dic_choice()
        print('\n')
        print_dashes(user_choice, location_keys, movie_keys, video_game_keys, famous_companie_keys)
        
        while chances > 0:
            pass
           



if __name__ == "__main__":
    main()
