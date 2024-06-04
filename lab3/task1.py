def solve_equation(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Ділення на нуль"

a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))

result = solve_equation(a, b)
print(f"Результат: {result}")
