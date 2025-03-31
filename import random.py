import random

number = random.randint(1, 100)
guess = int(input("Угадай число от 1 до 100: "))

print("Ты угадал!" if guess == number else f"Не угадал, было {number}")
