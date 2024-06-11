import random

def is_valid(number, upper_bound):
    try:
        num = int(number)
        return 1 <= num <= upper_bound
    except ValueError:
        return False

def play_game(upper_bound):
    attempts = 0
    number_to_guess = random.randint(1, upper_bound)
    print(f"Загадано число від 1 до {upper_bound}. Спробуйте вгадати!")

    while True:
        guess = input("Введіть ваше припущення: ")
        
        if not is_valid(guess, upper_bound):
            print(f"Будь ласка, введіть ціле число від 1 до {upper_bound}.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number_to_guess:
            print("Занадто мало, спробуйте ще раз.")
        elif guess > number_to_guess:
            print("Занадто багато, спробуйте ще раз.")
        else:
            print(f"Ви вгадали, вітаємо! Ви зробили {attempts} спроб(и).")
            break

while True:
    n = input("Введіть праву межу для випадкового вибору числа (мінімум 3): ")
    try:
        n = int(n)
        if n < 3:
            print("Межа повинна бути не меншою за 100.")
            continue
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        continue

    play_game(n)

    play_again = input("Бажаєте зіграти ще раз? (Y-так/N-ні): ").strip().upper()
    if play_again != 'Y':
        print("Дякуємо за гру!")
        break
