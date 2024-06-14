import random

# Створення списку зі 100 випадкових чисел
random_list = [random.randint(1, 1000) for _ in range(100)]

# Бульбашкове сортування
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Сортування вибором
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Сортування злиттям 
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def sort_func(sort_function, arr):
    sorted_arr = sort_function(arr.copy())
    return  sorted_arr

bubble_list = random_list.copy()
selection_list = random_list.copy()
merge_list = random_list.copy()

bubble_sorted = sort_func(bubble_sort, bubble_list)

selection_sorted = sort_func(selection_sort, selection_list)

merge_sorted = sort_func(merge_sort, merge_list)

assert bubble_sorted == sorted(random_list)
assert selection_sorted == sorted(random_list)
assert merge_sorted == sorted(random_list)

print("\nOriginal List:")
print(random_list)

print("\nBubble Sorted List:")
print(bubble_sorted)

print("\nSelection Sorted List:")
print(selection_sorted)

print("\nMerge Sorted List:")
print(merge_sorted)

