def create_spiral_matrix(n, m):
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    num = 1
    top = 0
    bottom = n - 1
    left = 0
    right = m - 1

    while num <= n * m:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix

def print_matrix(matrix):
    max_width = len(str(n * m))   

    for row in matrix:
        print(' '.join(f"{num:>{max_width}}" for num in row))

n, m = map(int, input("Введіть два натуральних числа n та m: ").split())

spiral_matrix = create_spiral_matrix(n, m)

print_matrix(spiral_matrix)
