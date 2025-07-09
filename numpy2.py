import numpy as np

array_manual = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
array_manual = np.array(array_manual)

value = array_manual[2][1]
alternate_rows = array_manual[::2]
reversed_rows = array_manual[::-1]
array_4x4 = np.arange(1, 17).reshape(4, 4)
max_value = array_4x4.max()
min_value = array_4x4.min()

print("Maximum value:", max_value)
print("Minimum value:", min_value)
print("4x4 Array:\n", array_4x4)
print("Reversed rows:\n", reversed_rows)
print("Alternate rows:\n", alternate_rows)
print("Value at 3rd row, 2nd column:", value)
print("2D Array:\n", array_manual)