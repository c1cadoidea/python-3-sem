def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

def calculate_f(a, b):
    f_value = (1 / (2 * a * b)) + (b ** 2) + 47 * a - ((a + 3 * b) ** 5)
    return f_value
    
fahrenheit_temp = calculate_f(2.9, 4.7)
celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp} градусів за Фаренгейтом відповідає {celsius_temp} градусів за Цельсієм")
