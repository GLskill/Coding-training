import random

number = random.randint(1, 100)

print("i have number at 1 to 100. Whot is this number.")

guesses = 0

while True:
    guess = int(input("Enter your guess: "))
    guesses += 1

    if guess == number:
        print("YES ! You guessed it ", guesses, "attempts!")
        break
    elif guess < number:
        print("this number is small.")
    else:
        print("this number is so BIG.")



