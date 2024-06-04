def find_middle(a, b, c):
    return (a + b + c) / 3

try:
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    c = int(input("Введіть третє число: "))

    if a != int(a) or b != int(b) or c != int(c):
        raise ValueError("Введіть цілі числа.")

    middle = find_middle(a, b, c)
    print(f"Середнє за величиною число: {middle}")
except ValueError as e:
    print(e)
