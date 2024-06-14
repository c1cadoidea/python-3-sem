def create_diagonal_matrix(n, m):
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    current_num = 1

    for i in range(n):
        row = i
        col = 0
        while row >= 0 and col < m:
            matrix[row][col] = current_num
            current_num += 1
            row -= 1
            col += 1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][j] = current_num
                current_num += 1

    return matrix

def print_diagonal_matrix(matrix):
    max_width = len(str(matrix[-1][-1]))   
    for row in matrix:
        print(' '.join(f"{num:>{max_width}}" for num in row))

n, m = map(int, input("Введіть два натуральних числа n та m: ").split())

diagonal_matrix = create_diagonal_matrix(n, m)

print_diagonal_matrix(diagonal_matrix)
