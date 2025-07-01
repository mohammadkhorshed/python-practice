# Number Guessing Game

import random
secret_number = random.randint(1, 100)
guess = 0
attempts = 0

print("Welcome to the Number Guessing Game!\nMy secret number is between 1 to 100!")

while guess != secret_number:
    try:
        guess = int(input("Enter you guess: "))
        attempts += 1

        if guess > secret_number:
            print("Too high!")
        elif guess < secret_number:
            print("Too low!")
        else:
            print(F"Congrats! You guessed the correct number \"{secret_number}\" in {attempts} attempts!")
    except ValueError:
        print("Invalid input! Please enter a valid number!")
