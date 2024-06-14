import re

def read_numbers(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
    numbers = re.findall(r'\b\d+\b', text)
    return [int(num) for num in numbers]

def calculate_sum(numbers):
    return sum(numbers)

def main():
    filename = "nums.txt"
    numbers = read_numbers(filename)
    total_sum = calculate_sum(numbers)
    print(f"Сума всіх чисел у файлі: {total_sum}")

if __name__ == "__main__":
    main()
