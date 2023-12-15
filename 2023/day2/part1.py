sum_ids = 0
max_color = {"r" : 12,  "g" : 13, "b" : 14}

with open("input") as f:
    for line in f:
        # grab the game id
        line = line.rstrip()
        line = line.lstrip("Game ")
        first_split = line.split(":")
        game_id = int(first_split[0])

        # split the number of shows via semicolon
        shows = first_split[1].split(";")

        # split the 3 colors by comma
        is_game_ok = True
        for show in shows:
            single = show.split(',')
            for color in single:
                check = color.strip().split(' ')
                if max_color[check[1][0]] < int(check[0]):
                    is_game_ok = False
                    break
        if is_game_ok:
            sum_ids = sum_ids + game_id

    print(sum_ids)
