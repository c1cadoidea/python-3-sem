def can_rook_move(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        return "YES"
    else:
        return "NO"

def get_coordinates():
    while True:
        try:
            x = int(input("Введіть номер стовпця (від 1 до 8): "))
            y = int(input("Введіть номер рядка (від 1 до 8): "))
            if 1 <= x <= 8 and 1 <= y <= 8:
                return x, y
            else:
                raise ValueError
        except ValueError:
            print("Помилка: координати повинні бути числами в діапазоні від 1 до 8. Спробуйте ще раз.")

print("Введіть координати першої клітини:")
x1, y1 = get_coordinates()

positions = [
    (1, 4),
    (1, 4),
    (1, 2),
    (8, 2)
]

for i, (x2, y2) in enumerate(positions, 1):
    result = can_rook_move(x1, y1, x2, y2)
    print(f"Перевірка {i}: Перша клітина ({x1}, {y1}), Друга клітина ({x2}, {y2}) -> {result}")
