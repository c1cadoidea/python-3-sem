def nth_term_geometric_progression(a1, r, n):
    return a1 * (r ** (n - 1))

# Приклад використання функції
a1 = float(input("Введіть перший член прогресії (a1): "))
r = float(input("Введіть знаменник прогресії (r): "))
n = int(input("Введіть порядковий номер члена прогресії (n): "))

nth_term = nth_term_geometric_progression(a1, r, n)
print(f"{n}-й член геометричної прогресії: {nth_term}")
