import random

def read_names():
    try:
        with open("names.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        return [line.strip() for line in lines]
    except FileNotFoundError:
        print("Файл names.txt не знайдено. Переконайтеся, що файл знаходиться в тій самій директорії, що й скрипт.")
        return []

def print_first_and_penultimate_and_your_surname(names, your_surname):
    if not names:
        return
    print(f"Перший рядок: {names[0]}")
    print(f"Передостанній рядок: {names[-2]}")
    for name in names:
        if your_surname in name:
            print(f"Рядок з вашим прізвищем: {name}")
            break

def print_random_line(names):
    if not names:
        return
    print(f"Випадковий рядок: {random.choice(names)}")

def print_reverse_lines(names):
    if not names:
        return
    print("Рядки у зворотному порядку:")
    for name in reversed(names):
        print(name)

def print_longest_and_shortest_lines(names):
    if not names:
        return
    longest = max(names, key=len)
    shortest = min(names, key=len)
    print(f"Найдовший рядок: {longest}")
    print(f"Найкоротший рядок: {shortest}")

def print_count_letters_words_lines(names):
    if not names:
        return
    num_lines = len(names)
    num_words = sum(len(line.split()) for line in names)
    num_letters = sum(len(line.replace(" ", "")) for line in names)
    print(f"Кількість рядків: {num_lines}")
    print(f"Кількість слів: {num_words}")
    print(f"Кількість літер: {num_letters}")

def main():
    your_surname = "Кордонський" 

    while True:
        names = read_names()
        if not names:
            break

        print_first_and_penultimate_and_your_surname(names, your_surname)
        print_random_line(names)
        print_reverse_lines(names)
        print_longest_and_shortest_lines(names)
        print_count_letters_words_lines(names)

        while True:
            repeat = input("Бажаєте виконати ще одну операцію? (Y/N): ").strip().upper()
            if repeat == 'Y':
                break
            elif repeat == 'N':
                print("Програма завершена.")
                return
            else:
                print("Будь ласка, введіть 'Y' або 'N'.")

if __name__ == "__main__":
    main()
