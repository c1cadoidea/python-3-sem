def determine_number_type(number):
    if number > 0:
        return "Позитивне число"
    elif number < 0:
        return "Негативне число"
    else:
        return "Нуль"

while True:
    user_input = input("Введіть число (або 'k' для виходу): ")
    
    if user_input.lower() == 'k':
        print("Вихід з програми.")
        break
    
    try:
        number = float(user_input)
        result = determine_number_type(number)
        print(f"Введене число є: {result}")
    except ValueError:
        print("Будь ласка, введіть правильне число або 'k' для виходу.")
