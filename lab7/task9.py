def is_magic_square(matrix):
    n = len(matrix)
    target_sum = n * (n**2 + 1) // 2  

    for i in range(n):
        row_sum = sum(matrix[i])
        col_sum = sum(matrix[j][i] for j in range(n))
        if row_sum != target_sum or col_sum != target_sum:
            return False

    diag_sum1 = sum(matrix[i][i] for i in range(n))
    diag_sum2 = sum(matrix[i][n-1-i] for i in range(n))
    if diag_sum1 != target_sum or diag_sum2 != target_sum:
        return False

    return True

n = int(input("Введіть розмірність квадратної матриці: "))

print("Введіть елементи матриці, розділені пробілами:")
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

if is_magic_square(matrix):
    print("YES")
else:
    print("NO")
