with open("input.txt", "r") as f:
    pipe_tiles = [line.strip() for line in f.read().strip().splitlines()]

animal_pos = [[i, row.index("S")] for i, row in enumerate(pipe_tiles) if "S" in row][0]

main_loop_map = [
    [False for _ in range(len(pipe_tiles[0]))] for _ in range(len(pipe_tiles))
]

main_loop_map[animal_pos[0]][animal_pos[1]] = True


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
                to_discover.append((surrounding_pos))


discover_surroundings(animal_pos)
print(sum(row.count(True) for row in main_loop_map) // 2)
