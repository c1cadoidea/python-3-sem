def first_digit_after_decimal(number):
    fractional_part = number - int(number)
    first_digit = int(fractional_part * 10)
    return first_digit

number = 1254.86
first_digit = first_digit_after_decimal(number)
print(f"Перша цифра після десяткової точки числа {number}: {first_digit}")
