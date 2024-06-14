import csv

def read_csv(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data

def display_data(data):
    for entry in data:
        print(entry)

def main():
    filename = "data.csv"
    while True:
        print("\nМеню:")
        print("1. Прочитати та вивести дані з CSV файлу")
        print("2. Вийти")
        choice = input("Виберіть опцію (1 або 2): ")

        if choice == '1':
            data = read_csv(filename)
            display_data(data)
        elif choice == '2':
            print("Завершення програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
