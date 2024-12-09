safe_reports = 0
unsafe_reports = []
valid_increasing = {1, 2, 3}
valid_decreasing = {-1, -2, -3}

def is_report_safe(report):
    differences = {report[i] - report[i+1] for i in range(0, len(report) - 1)}
    return differences <= valid_increasing or differences <= valid_decreasing

reports = []
with open("input.txt") as f:
    for _, line in enumerate(f):
        split_data = line.strip().split(' ')
        report = [int(i) for i in split_data]
        reports.append(report)

for report in reports:
    if (is_report_safe(report)):
        safe_reports += 1

print(f'Part 1: {safe_reports}')

problem_dampner = 0
for report in reports:
    if (is_report_safe(report)):
        problem_dampner += 1
        continue

    for i in range(len(report)):
        if(is_report_safe(report[:i] + report[i+1:])):
            problem_dampner += 1
            break
print(f'Part 2: {problem_dampner}')
