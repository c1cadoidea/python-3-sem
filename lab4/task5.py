while True:
    user_input = input("Введіть натуральне число або 'q' для виходу: ")
    if user_input.lower() == 'q':
        break
    
    if not user_input.isdigit() or int(user_input) == 0:
        print("Помилка: введіть натуральне число (ціле додатнє число) або 'q' для виходу")
        continue
    
    number = user_input
    digits = [int(digit) for digit in number]
    
    max_digit = max(digits)
    min_digit = min(digits)
    
    print(f"Число {number} містить максимальну цифру {max_digit} та мінімальну цифру {min_digit}.")
