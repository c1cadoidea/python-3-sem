def sort_array(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

numbers = []

for i in range(4):
    num = float(input(f"Введіть число {i+1}: "))
    numbers.append(num)

sorted_numbers = sort_array(numbers)

print(f"Найменше число: {sorted_numbers[0]}")
print(f"Найбільше число: {sorted_numbers[-1]}")
