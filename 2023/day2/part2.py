final = 0

def reset_dict():
    return {"r" : 0, "g" : 0, "b": 0}

with open("input") as f:
    for line in f:
        line = line.rstrip()

        max_color = reset_dict()

        shows = line.split(":")[1].split(";")

        for show in shows:
            single = show.split(',')
            for color in single:
                check = color.strip().split(' ')
                if max_color[check[1][0]] < int(check[0]):
                    max_color[check[1][0]] = int(check[0])

        product = 1
        for _, value in max_color.items():
            product = product * value

        final = final + product
    print(final)
