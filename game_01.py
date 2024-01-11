import random

number = random.randint(1, 100)

print("Я загадал число от 1 до 100. Попробуйте его угадать.")

guesses = 0

while True:
    guess = int(input("Введите ваше предположение: "))
    guesses += 1

    if guess == number:
        print("Поздравляю! Вы угадали число за", guesses, "попыток!")
        break
    elif guess < number:
        print("Ваше предположение слишком мало.")
    else:
        print("Ваше предположение слишком велико.")



