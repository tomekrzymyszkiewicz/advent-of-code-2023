from colorama import Fore, Back
with open("input.txt", "r") as f:
    pipe_tiles = [line.strip() for line in f.read().strip().splitlines()]

animal_pos = [[i, row.index("S")] for i, row in enumerate(pipe_tiles) if "S" in row][0]

main_loop_map = [
    [False for _ in range(len(pipe_tiles[0]))] for _ in range(len(pipe_tiles))
]

main_loop_map[animal_pos[0]][animal_pos[1]] = True
polygon_coordinates = [animal_pos]


def is_connected(curr_pos: list[int], adj_pos: list[int]) -> bool:
    if (
        adj_pos[0] < 0
        or adj_pos[0] >= len(pipe_tiles)
        or adj_pos[1] < 0
        or adj_pos[1] >= len(pipe_tiles[0])
    ):
        return False
    else:
        if main_loop_map[adj_pos[0]][adj_pos[1]] is True:
            return False
        if (
            adj_pos[0] < curr_pos[0]
            and pipe_tiles[curr_pos[0]][curr_pos[1]] in "|JLS"
            and pipe_tiles[adj_pos[0]][adj_pos[1]] in "|F7S"
        ):  # above
            return True
        elif (
            adj_pos[0] > curr_pos[0]
            and pipe_tiles[curr_pos[0]][curr_pos[1]] in "|F7S"
            and pipe_tiles[adj_pos[0]][adj_pos[1]] in "|JLS"
        ):  # below
            return True
        elif (
            adj_pos[1] < curr_pos[1]
            and pipe_tiles[curr_pos[0]][curr_pos[1]] in "-J7S"
            and pipe_tiles[adj_pos[0]][adj_pos[1]] in "-FLS"
        ):  # to left
            return True
        elif (
            adj_pos[1] > curr_pos[1]
            and pipe_tiles[curr_pos[0]][curr_pos[1]] in "-FLS"
            and pipe_tiles[adj_pos[0]][adj_pos[1]] in "-J7S"
        ):  # to right
            return True
        return False


def discover_surroundings(pos: list[int]) -> None:
    to_discover = [pos]
    while to_discover:
        curr_pos = to_discover.pop()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            surrounding_pos = [curr_pos[0] + dx, curr_pos[1] + dy]
            if is_connected(curr_pos, surrounding_pos):
                main_loop_map[surrounding_pos[0]][surrounding_pos[1]] = True
                polygon_coordinates.append(surrounding_pos)
                to_discover.append((surrounding_pos))
    polygon_coordinates[0], polygon_coordinates[1] = (
        polygon_coordinates[1],
        polygon_coordinates[0],
    )


def count_internal_tiles(pipe_tiles_loop):
    boundries_mapping = [("-", ""), ("LJ", ""), ("F7", ""), ("L7", "|"), ("FJ", "|")]
    internal_tiles_map = main_loop_map = [
        [False for _ in range(len(pipe_tiles[0]))] for _ in range(len(pipe_tiles))
    ]
    for i in range(len(main_loop_map)):
        for j in range(len(main_loop_map[0])):
            checked_tile = main_loop_map[i][j]
            if not checked_tile:
                row_to_left = "".join(pipe_tiles_loop[i][:j])
                row_to_right = "".join(pipe_tiles_loop[i][j + 1 :])
                for mapping, replace_string in boundries_mapping:
                    row_to_left = row_to_left.replace(mapping, replace_string)
                    row_to_right = row_to_right.replace(mapping, replace_string)
                number_of_boundires_to_right = row_to_left.count("|")
                number_of_boundires_to_left = row_to_right.count("|")
                if (
                    number_of_boundires_to_right % 2 == 1
                    and number_of_boundires_to_left % 2 == 1
                ):
                    internal_tiles_map[i][j] = True
    return internal_tiles_map


def replace_S(animal_pos, pipe_tiles_loop):
    right, left, above, below = False, False, False, False
    if (
        animal_pos[1] + 1 < len(pipe_tiles[0])
        and pipe_tiles_loop[animal_pos[0]][animal_pos[1] + 1] in "-7J"
    ):
        right = True
    if (
        animal_pos[1] - 1 > 0
        and pipe_tiles_loop[animal_pos[0]][animal_pos[1] - 1] in "-FL"
    ):
        left = True
    if (
        animal_pos[0] - 1 > 0
        and pipe_tiles_loop[animal_pos[0] - 1][animal_pos[1]] in "|F7"
    ):
        above = True
    if (
        animal_pos[0] + 1 < len(pipe_tiles)
        and pipe_tiles_loop[animal_pos[0] + 1][animal_pos[1]] in "|LJ"
    ):
        below = True
    if below and right:
        pipe_tiles_loop[animal_pos[0]][animal_pos[1]] = "F"
    elif below and left:
        pipe_tiles_loop[animal_pos[0]][animal_pos[1]] = "7"
    elif above and right:
        pipe_tiles_loop[animal_pos[0]][animal_pos[1]] = "L"
    elif above and left:
        pipe_tiles_loop[animal_pos[0]][animal_pos[1]] = "J"
    elif above and below:
        pipe_tiles_loop[animal_pos[0]][animal_pos[1]] = "|"
    elif left and right:
        pipe_tiles_loop[animal_pos[0]][animal_pos[1]] = "-"
    return pipe_tiles_loop

def print_colored_map(pipe_tiles_loop, internal_tiles_map):
    for i,row in enumerate(pipe_tiles_loop):
        colored_row = []
        for j,tile in enumerate(row):
            if tile == '.' and internal_tiles_map[i][j]:
                colored_row.extend([Fore.BLUE,Back.BLUE,tile,Back.RESET,Fore.RESET])
            elif tile == '.':
                colored_row.extend([Fore.WHITE,Back.WHITE,tile,Back.RESET,Fore.RESET])
            elif tile in '-|FJ7L':
                colored_row.extend([Fore.GREEN,Back.GREEN,tile,Back.RESET,Fore.RESET])
        print(''.join(colored_row))
        

discover_surroundings(animal_pos)
pipe_tiles_loop = [
    [tile if main_loop_map[i][j] else "." for j, tile in enumerate(row)]
    for i, row in enumerate(pipe_tiles)
]
pipe_tiles_loop = replace_S(animal_pos, pipe_tiles_loop)
internal_tiles_map = count_internal_tiles(pipe_tiles_loop)
print_colored_map(pipe_tiles_loop, internal_tiles_map)