def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sum_of_factorials(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total

while True:
    user_input = input("Введіть число n або 'k' для виходу: ")
    if user_input.lower() == 'k':
        break
    try:
        n = int(user_input)
        if n < 0:
            print("Помилка: n повинно бути невід'ємним цілим числом")
        else:
            result = sum_of_factorials(n)
            print(f"Сума факторіалів від 1 до {n}: {result}")
    except ValueError:
        print("Помилка: введіть ціле число або 'k' для виходу")
