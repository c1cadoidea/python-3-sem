def fibonacci_sequence(n):
    sequence = [1, 1]
    for i in range(2, n):
        next_fib = sequence[-1] + sequence[-2]
        sequence.append(next_fib)
    return sequence

while True:
    try:
        user_input = input("Введіть натуральне число n (10 < n < 30) або 'q' для виходу: ")
        if user_input.lower() == 'q':
            break
        n = int(user_input)
        if 10 < n < 30:
            fib_sequence = fibonacci_sequence(n)
            print(f"Перші {n} чисел послідовності Фібоначчі: {fib_sequence}")
        else:
            print("Помилка: n повинно бути в межах від 10 до 30.")
    except ValueError:
        print("Помилка: введіть ціле число або 'q' для виходу.")
