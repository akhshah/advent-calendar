calibration = 0
with open("input") as f:
    for _, line in enumerate(f):
        n = [int(n) for n in line if n.isdigit()]
        calibration = calibration + n[0] * 10 + n[-1]

print(calibration)

calibration = 0
string_number_dict = {"one" : 1, "two" : 2, "three" : 3, "four" : 4,
                      "five" : 5, "six" : 6, "seven" : 7, "eight" : 8,
                      "nine" : 9}
#  with open("input") as f:

def find_digit(substring):
    if substring[0].isdigit():
        return int(substring[0])

    for key, value in string_number_dict.items():
        if substring.startswith(key):
            return value


with open("input") as f:
    for line in f:
        first = second = None
        for i, _ in enumerate(line):
            if first == None:
                first = find_digit(line[i:])
            if second == None:
                second = find_digit(line[len(line) - i - 1:])

            if first != None and second != None:
                break

        calibration = calibration + first * 10 + second
print(calibration)
