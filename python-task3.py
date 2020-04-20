import random

while True:
    level = input("Choose your level (easy, medium or hard): ")
    if level == "easy":
        guess_limit = 6
        secret_number = random.randint(1, 10)
        break
    elif level == "medium":
        guess_limit = 4
        secret_number = random.randint(1, 20)
        print(secret_number)
        break
    elif level == "hard":
        guess_limit = 3
        secret_number = random.randint(1, 50)
        print(secret_number)
        break
    else:
        continue

guess_count = 1
while guess_count <= guess_limit :
    guess = int(input("Guess the secret number from 1 - 10: "))
    if guess == secret_number :
        print("You got it right")
        break
    else :
        remaining_guesses = guess_limit - guess_count
        if remaining_guesses > 0:
            print(f"That was wrong. You have {remaining_guesses} guesses left")
        guess_count += 1
else:
    print("Game Over!")