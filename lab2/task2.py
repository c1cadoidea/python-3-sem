def calculate_f(a, b):
    f_value = (1 / (2 * a * b)) + (b ** 2) + 47 * a - ((a + 3 * b) ** 5)
    return f_value

a = 2.9
b = 4.7

result = calculate_f(a, b)
print(f"f({a}, {b}) = {result}")

