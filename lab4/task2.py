while True:
    user_input = input("Введіть натуральне число або 'q' для виходу: ")
    if user_input.lower() == 'q':
        break
    
    if not user_input.isdigit() or int(user_input) == 0:
        print("Помилка: введіть натуральне число (ціле додатнє число) або 'q' для виходу")
        continue
    
    number = int(user_input)
    even_digits = []
    odd_digits = []
    
    for digit in str(number):
        if int(digit) % 2 == 0:
            even_digits.append(digit)
        else:
            odd_digits.append(digit)
    
    even_count = len(even_digits)
    odd_count = len(odd_digits)
    
    print(f"Число {number} містить {even_count} парних цифр(и) ({', '.join(even_digits)}) та {odd_count} непарних цифр(и) ({', '.join(odd_digits)}).")
