def position_to_coordinates(position):
    col = ord(position[0].lower()) - ord('a')
    row = int(position[1]) - 1
    return row, col

def coordinates_to_position(row, col):
    return chr(col + ord('a')) + str(row + 1)

def print_chessboard(knight_position):
    chessboard = [['.' for _ in range(8)] for _ in range(8)]
    knight_row, knight_col = knight_position

    chessboard[knight_row][knight_col] = 'N'

    moves = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2),
        (2, -1), (2, 1)
    ]

    for move in moves:
        new_row = knight_row + move[0]
        new_col = knight_col + move[1]
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            chessboard[new_row][new_col] = '*'

    for row in chessboard:
        print(' '.join(row))

knight_position_input = input("Введіть положення коня (літера та цифра): ")
knight_position = position_to_coordinates(knight_position_input)

print("Шахова дошка з позначеним положенням коня та клітинами, які він б'є:")
print_chessboard(knight_position)
