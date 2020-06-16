#Test
import time

def greeting():
    print("Welcome to our Hangman game!\nYou will be playing against a computer.")

def dic_choice():
    choice = input("Would you like to play 1. Locations 2. Movies 3. Video Games 4. Famous Companies")

def main():
    game_on = True
    locations = {"Paris": 5, "Brussels": 8, "London": 6, "Chicago": 7, "New York City": 11}
    movies = {"Matrix": 6, "Inception": 9, "Venom": 5, "Star Wars": 8, "The Godfather": 12}
    video_games = {"Fornite": 7, "Warzone": 7, "FIFA": 4, "Minecraft": 9, "Pac Man": 6}
    famous_companies = {"Apple": 5, "Microsoft": 9, "Oracle": 6, "Nike": 4, "Tesla": 5}
    while game_on:
        chances = 6
        greeting()
        while chances > 0:
           pass 
        if game_on:
            pass
        else:
            break


if __name__ == "__main__":
    main()
