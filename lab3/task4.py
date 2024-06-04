def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "ТАК"
    else:
        return "НІ"

while True:
    user_input = input("Введіть рік (або 'k' для виходу): ")
    
    if user_input.lower() == 'k':
        print("Вихід з програми.")
        break
    
    try:
        year = int(user_input)
        result = is_leap_year(year)
        print(f"{year} {result}")
    except ValueError:
        print("Будь ласка, введіть правильний рік або 'k' для виходу.")
