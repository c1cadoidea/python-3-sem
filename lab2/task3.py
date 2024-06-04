def calculs(num1, num2):
    sum = num1 + num2
    diff = num1 - num2
    prod = num1 * num2
    return sum, diff, prod

num1 = int(input("Введіть число народження: "))
num2 = int(input("Введіть місяць народження: "))

sum, diff, prod = calculs(num1, num2)
print(f"Сума: {sum}")
print(f"Різниця: {diff}")
print(f"Добуток: {prod}")
