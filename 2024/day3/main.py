import re

pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
pattern_digits = re.compile(r'\d{1,3}')

checksum = 0
# Part 2
with open('input.txt') as f:
    for line in f:
        matches = re.findall(pattern, line)

        for match in matches:
            digits = re.findall(pattern_digits, match)
            val = 1
            for digit in digits:
                val *= int(digit)
            checksum += val
print(checksum)

# Part 2
pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)')
do_string = "do()"
dont_string = "don't()"
multiply = True

part2 = 0
with open('input.txt') as f:
    for line in f:
        matches = re.findall(pattern, line)
        for match in matches:
            if match == "do()":
                multiply = True
                continue
            elif match == "don't()":
                multiply = False
                continue

            if multiply:
                digits = re.findall(pattern_digits, match)
                val = 1
                for digit in digits:
                    val *= int(digit)
                part2 += val
print(part2)




