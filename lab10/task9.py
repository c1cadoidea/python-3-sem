import random

def generate_random_numbers(filename, count, min_value, max_value):
    with open(filename, "w", encoding="utf-8") as file:
        for _ in range(count):
            number = random.randint(min_value, max_value)
            file.write(f"{number}\n")

def main():
    filename = "random.txt"
    count = 2525
    min_value = 111
    max_value = 777

    generate_random_numbers(filename, count, min_value, max_value)
    print(f"Згенеровано {count} випадкових чисел у діапазоні від {min_value} до {max_value} та записано у файл {filename}.")

if __name__ == "__main__":
    main()
