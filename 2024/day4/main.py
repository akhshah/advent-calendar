array = []
#  with open('input.txt') as f:
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        array.append([])
        for char in line:
            array[-1].append(char)

directions = [[1, 0],
              [1, 1],
              [0, 1],
              [-1, 1],
              [-1, 0],
              [-1, -1],
              [0, -1],
              [1, -1]]

xmas_number = 0
def check_range(curr_pos, direction, max_width, max_height):
    new_pos = [curr_pos[0] + direction[0], curr_pos[1] + direction[1]]

    if (new_pos[0] < 0 or new_pos[1] < 0):
        return False
    if (new_pos[0] >= max_width):
        return False
    if (new_pos[1] >= max_height):
        return False

    return True

def search(array, curr_pos, direction, search_pattern):
    if (not search_pattern):
        return 1

    if (not check_range(curr_pos, direction, len(array), len(array[curr_pos[0]]))):
        return 0

    new_pos = [curr_pos[0] + direction[0], curr_pos[1] + direction[1]]

    if (array[new_pos[0]][new_pos[1]] != search_pattern[0]):
        return 0

    return search(array, new_pos, direction, search_pattern[1:])

search_pattern = "MAS"
for i in range(0, len(array)):
    for j in range(0, len(array[i])):
        if array[i][j] == 'X':
            for direction in directions:
                xmas_number += search(array, [i, j], direction, search_pattern)

print(xmas_number)

search_pattern2 = "SAM"
xmas_number2 = 0
for i in range(1, len(array) - 1):
    if (i - 1 < 0 or i + 1 >= len(array)):
        continue
    for j in range(1, len(array[i]) - 1):
        if (j - 1 < 0 or j + 1 >= len(array[i])):
            continue

        first_diag = "".join([array[i-1][j-1], array[i][j], array[i+1][j+1]])
        second_diag = "".join([array[i-1][j+1], array[i][j], array[i+1][j-1]])

        first_match = first_diag == search_pattern or first_diag == search_pattern2
        second_match = second_diag == search_pattern or second_diag == search_pattern2

        if (first_match and second_match):
            xmas_number2 += 1

print(xmas_number2)
