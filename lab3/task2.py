import math

def calculate_y(x):
    if x < 0:
        return abs(x)
    elif x > 0:
        return math.sqrt(x)
    else:
        return 0  

x = float(input("Введіть значення x: "))

y = calculate_y(x)
print(f"Значення y: {y}")
