import random

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Enter your guess (1-100): ")

    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if not 1 <= guess <= 100:
        print("Out of range. Please enter a number between 1 and 100.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print(f"Correct! You guessed the number in {attempts} attempts.")
        break
