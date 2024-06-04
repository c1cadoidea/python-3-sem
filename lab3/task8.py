def determine_color(pocket_number):
    if pocket_number == 0:
        return "Зелена"
    elif 1 <= pocket_number <= 10:
        return "Червона" if pocket_number % 2 != 0 else "Чорна"
    elif 11 <= pocket_number <= 18:
        return "Чорна" if pocket_number % 2 != 0 else "Червона"
    elif 19 <= pocket_number <= 28:
        return "Червона" if pocket_number % 2 != 0 else "Чорна"
    elif 29 <= pocket_number <= 36:
        return "Чорна" if pocket_number % 2 != 0 else "Червона"
    else:
        return "Помилка: номер кишені має бути від 0 до 36"

while True:
    user_input = input("Введіть номер кишені (від 0 до 36) або 'k' для виходу: ")
    if user_input.lower() == 'k':
        break
    try:
        pocket_number = int(user_input)
        print(determine_color(pocket_number))
    except ValueError:
        print("Помилка: введіть ціле число або 'k' для виходу")
