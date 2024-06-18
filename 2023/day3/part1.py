from library import extract_into_array

def recurse(array, position):
    height = len(array)
    width = len(array[0])

    if 

array = extract_into_array("input.txt")
traversed = []

len_row = len(array[0])
for i, _ in enumerate(array):
    traversed.append([None] * len_row)

for i, line in enmerate(array):
    for j, val in enumerate(line):
        if traversed[i][j] == True:
            continue

        if val == '.':
            traversed = 
