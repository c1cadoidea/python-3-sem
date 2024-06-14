def pascal_triangle_row(n):
    row = [1]
    for i in range(1, n + 1):
        next_row = [1]
        for j in range(1, i):
            next_row.append(row[j - 1] + row[j])
        next_row.append(1)
        row = next_row
    return row

def draw_pascal_triangle(n):
    max_width = len(' '.join(map(str, pascal_triangle_row(n))))

    for i in range(n + 1):
        row = pascal_triangle_row(i)
        padding = " " * ((max_width - len(' '.join(map(str, row)))) // 2)
        print(f"{i}: {padding}{' '.join(map(str, row))}")

n = int(input("Введіть номер рядка трикутника Паскаля: "))
print("Трикутник Паскаля до", n, "рядка :")
draw_pascal_triangle(n)
print("Рядок №", n, ":")
print(pascal_triangle_row(n))
