while True:
    user_input = input("Введіть непарне натуральне число n (порядковий номер місяця народження студента) або 'q' для виходу: ")
    if user_input.lower() == 'q':
        break
    
    try:
        n = int(user_input)
        if n % 2 == 0 or n <= 0:
            print("Помилка: n повинно бути непарним натуральним числом.")
            continue
        
        # Виведення трикутника
        for i in range(1, (n // 2) + 2):
            print('*' * i)
        for i in range((n // 2), 0, -1):
            print('*' * i)
        
    except ValueError:
        print("Помилка: введіть ціле непарне натуральне число або 'q' для виходу.")
