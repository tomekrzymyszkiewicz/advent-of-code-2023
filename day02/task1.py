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
print(games)

def reveal_exceed_limit(reveal: dict) -> bool:
    for color, value in reveal.items():
        if limits[color] < value:
            return True
    return False

def if_game_possible(game: list) -> bool:
    for reveal in game:
        if reveal_exceed_limit(reveal):
            return False
    return True

possible_count = 0
for game_id, game in games.items():
    if if_game_possible(game):
        print(f'{game_id = }')
        possible_count += game_id

print(possible_count)
