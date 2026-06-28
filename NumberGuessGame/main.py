import random

secret_number = random.randint(1, 100)

print("Welcome to Number Guessing Game!")

while True:

    guess = int(input("Enter your guess (1-100): "))

    if guess == secret_number:
        print("Congratulations!")
        print("You guessed correctly.")
        break

    elif guess > secret_number:
        print("Too High!")

    else:
        print("Too Low!")