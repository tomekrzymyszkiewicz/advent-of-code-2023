import math
with open('input.txt','r') as f:
    lines = f.readlines()
limits = {'red':12,'green':13,'blue':14}


games = {int(line.split(':')[0].split(' ')[1]):line.split(':')[1] for line in lines}
for game_id, game in games.items():
    reveals_line = game.split(';')
    reveals = []
    for reveal in reveals_line:
        cubes = reveal.split(',')
        reveal_result = {}
        for cube in cubes:
            value, color = cube.strip().split(' ')
            reveal_result[color] = int(value)
        reveals.append(reveal_result)
    games[game_id] = reveals

counter = 0
for game_id, game in games.items():
    max_values = {'red':-1,'blue':-1,'green':-1}
    for reveal in game:
        for color, value in reveal.items():
            if max_values[color] < value:
                max_values[color] = value
    games[game_id] = max_values
    counter += math.prod(max_values.values())



print(counter)
