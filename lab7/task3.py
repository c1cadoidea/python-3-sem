def create_list_of_lists(n):
    result = []
    for i in range(1, n + 1):
        sublist = list(range(1, i + 1))
        result.append(sublist)
    return result

n = int(input("Введіть число n: "))
list_of_lists = create_list_of_lists(n)

print("Результат:")
print(list_of_lists)
