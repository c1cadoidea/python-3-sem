def max_element_shaded(matrix):
    n = len(matrix)
    max_element = float('-inf')  

    for i in range(n):
        for j in range(n):
            if j <= i <= n - 1 - j or j >= i >= n - 1 - j:  
                max_element = max(max_element, matrix[i][j])

    return max_element

n = int(input("Введіть розмірність квадратної матриці: "))

print("Введіть елементи матриці, розділені пробілами:")
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

result = max_element_shaded(matrix)
print("Максимальний елемент у заштрихованій області:", result)
