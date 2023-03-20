import random


def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have to guess what that number is. Good luck!")

    number = random.randint(1, 100)
    attempts = 0
    while True:
        guess_before_int = input("Enter your guess and insert a number between 1 and 100: ")
        attempts += 1
        if type(guess_before_int) != int:
            continue
        else:
            guess = int(guess_before_int)
        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break


start_game()
