
unprocessed_rules = []
updates = []
process_updates = False

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if (line == ""):
            process_updates = True
            continue

        if process_updates:
            updates.append(line.split(','))
            continue

        unprocessed_rules.append(line.split('|'))

print(updates[0])
print(unprocessed_rules[0])
