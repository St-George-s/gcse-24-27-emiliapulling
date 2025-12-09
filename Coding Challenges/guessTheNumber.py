import random
number = random.randint(1,51)
guess = int(input("Guess the number! "))
while guess != number:
    if guess > number:
        print("Too high!")
        guess = int(input("Guess the number! "))
    elif guess < number:
        print("Too low!")
        guess = int(input("Guess the number! "))
print("Well done! You guessed the correct number!")
