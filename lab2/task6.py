def manhattan_distance(point1, point2):
    p1, p2 = point1
    q1, q2 = point2
    distance = abs(p1 - q1) + abs(p2 - q2)
    return distance

point1 = (2, 12)
point2 = (18, 19)
distance = manhattan_distance(point1, point2)
print(f"Манхеттенська відстань між {point1} і {point2} = {distance}")
