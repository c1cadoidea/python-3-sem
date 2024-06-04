def cube_properties(edge_length):
    volume = edge_length ** 3
    area = 6 * (edge_length ** 2)
    return volume, area

edge_length = 7
volume, area = cube_properties(edge_length)
print("Об'єм куба: {}".format(volume))
print("Площа повної поверхні куба: {}".format(area))
