# Extract input data
# data is stored in two columns and must be compared against one another.
data = []
data.append([])
data.append([])

with open("input.txt") as f:
    for _, line in enumerate(f):
        split_data = line.strip().split(' ')
        data[0].append(split_data[0])
        data[1].append(split_data[-1])

list1 = data[0]
list2 = data[1]

sorted_list = sorted(list1)
sorted_list2 = sorted(list2)

# Problem 1 solution
total_distance = 0
for item in zip(sorted_list, sorted_list2):
    total_distance += abs(int(item[0]) - int(item[1]))

print(total_distance)

# Problem 2 solution
similarity_score = 0

import collections
counter = collections.Counter(list2)
frequency = dict(counter)

for item in list1:
    freq = frequency.get(item, 0)
    similarity_score += int(item) * int(freq)

print(similarity_score)
