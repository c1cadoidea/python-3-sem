def chunked(lst, size):
    chunked_list = []
    for i in range(0, len(lst), size):
        chunked_list.append(lst[i:i+size])
    return chunked_list

input_str = input("Введіть список символів через пробіл: ").split()
n = int(input("Введіть розмір чанка: "))

result = chunked(input_str, n)
print("Результат:", result)
