import math

class Sphere:
    def __init__(self, radius=1.0, x=0.0, y=0.0, z=0.0):
        self.radius = radius
        self.center = (x, y, z)

    def get_volume(self) -> float:
        return (4/3) * math.pi * (self.radius ** 3)

    def get_square(self) -> float:
        return 4 * math.pi * (self.radius ** 2)

    def get_radius(self) -> float:
        return self.radius

    def get_center(self) -> tuple:
        return self.center

    def set_radius(self, r: float):
        self.radius = r

    def set_center(self, x: float, y: float, z: float):
        self.center = (x, y, z)

    def is_point_inside(self, x: float, y: float, z: float) -> bool:
        distance = math.sqrt((x - self.center[0]) ** 2 +
                             (y - self.center[1]) ** 2 +
                             (z - self.center[2]) ** 2)
        return distance <= self.radius


def create_sphere_from_input() -> Sphere:
    print("Створення сфери:")
    radius = float(input("Введіть радіус сфери (за замовчуванням 1): ") or 1)
    x = float(input("Введіть координату x центру сфери (за замовчуванням 0): ") or 0)
    y = float(input("Введіть координату y центру сфери (за замовчуванням 0): ") or 0)
    z = float(input("Введіть координату z центру сфери (за замовчуванням 0): ") or 0)
    return Sphere(radius, x, y, z)

def main():
    sphere = create_sphere_from_input()
    
    print("\nІнформація про сферу:")
    print("Об'єм кулі:", sphere.get_volume())
    print("Площа поверхні кулі:", sphere.get_square())
    print("Радіус кулі:", sphere.get_radius())
    print("Центр кулі:", sphere.get_center())

    while True:
        print("\nМеню:")
        print("1. Встановити новий радіус")
        print("2. Встановити новий центр")
        print("3. Перевірити, чи точка всередині кулі")
        print("4. Вийти")

        choice = input("Виберіть опцію: ")
        if choice == '1':
            new_radius = float(input("Введіть новий радіус: "))
            sphere.set_radius(new_radius)
            print("Новий радіус встановлено.")
        elif choice == '2':
            new_x = float(input("Введіть нову координату x центру: "))
            new_y = float(input("Введіть нову координату y центру: "))
            new_z = float(input("Введіть нову координату z центру: "))
            sphere.set_center(new_x, new_y, new_z)
            print("Новий центр встановлено.")
        elif choice == '3':
            point_x = float(input("Введіть координату x точки: "))
            point_y = float(input("Введіть координату y точки: "))
            point_z = float(input("Введіть координату z точки: "))
            if sphere.is_point_inside(point_x, point_y, point_z):
                print("Точка знаходиться всередині кулі.")
            else:
                print("Точка знаходиться за межами кулі.")
        elif choice == '4':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
