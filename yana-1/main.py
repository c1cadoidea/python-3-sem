import numpy as np

def unravel_index_custom(index, shape):
    coords = []
    for dim_size in reversed(shape):
        coords.append(index % dim_size)
        index //= dim_size
    return tuple(reversed(coords))

element_number = 9
shape = (2, 3, 2)

index = unravel_index_custom(element_number, shape)
print(index)
