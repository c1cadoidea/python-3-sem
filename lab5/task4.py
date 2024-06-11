import math

def solve(a, b, c):
    D = b**2 - 4*a*c

    if D < 0:
        return "Рівняння не має дійсних коренів"
    elif D == 0:
        x1 = -b / (2*a)
        return (x1,)
    else:
        sqrt_D = math.sqrt(D)
        x1 = (-b - sqrt_D) / (2*a)
        x2 = (-b + sqrt_D) / (2*a)
        return (min(x1, x2), max(x1, x2))

a = int(input("Введіть коефіцієнт a: "))
b = int(input("Введіть коефіцієнт b: "))
c = int(input("Введіть коефіцієнт c: "))

roots = solve(a, b, c)
print(f"Корені рівняння: {roots}")
