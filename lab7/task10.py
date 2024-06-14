def create_snake_matrix(n, m):
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    current_num = 1

    for i in range(n):
        if i % 2 == 0:
            for j in range(m):
                matrix[i][j] = current_num
                current_num += 1
        else:
            for j in range(m - 1, -1, -1):
                matrix[i][j] = current_num
                current_num += 1

    return matrix

def print_snake_matrix(matrix):
    for row in matrix:
        print(''.join(f"{num:<3}" for num in row))

n, m = map(int, input("Введіть два натуральних числа n та m: ").split())

snake_matrix = create_snake_matrix(n, m)

print_snake_matrix(snake_matrix)
