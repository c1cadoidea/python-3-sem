while True:
    user_input = input("Введіть натуральне число або 'q' для виходу: ")
    if user_input.lower() == 'q':
        break
    
    if not user_input.isdigit() or int(user_input) == 0:
        print("Помилка: введіть натуральне число (ціле додатнє число) або 'q' для виходу")
        continue
    
    number = user_input
    digits = [int(digit) for digit in number]
    
    sum_of_digits = sum(digits)
    count_of_digits = len(digits)
    product_of_digits = 1
    for digit in digits:
        product_of_digits *= digit
    
    average_of_digits = sum_of_digits / count_of_digits
    first_digit = digits[0]
    last_digit = digits[-1]
    sum_first_last = first_digit + last_digit
    
    print(f"Число {number} має такі характеристики:")
    print(f"Сума цифр: {sum_of_digits}")
    print(f"Кількість цифр: {count_of_digits}")
    print(f"Твір цифр: {product_of_digits}")
    print(f"Середнє арифметичне цифр: {average_of_digits}")
    print(f"Перша цифра: {first_digit}")
    print(f"Сума першої та останньої цифри: {sum_first_last}")
