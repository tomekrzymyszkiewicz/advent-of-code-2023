from types import SimpleNamespace

with open("input.txt", "r") as f:
    input = f.read().strip().splitlines()


moves = SimpleNamespace(
    **{"right": (0, 1), "left": (0, -1), "up": (-1, 0), "down": (1, 0)}
)

slash_moves_map = {
    moves.right: moves.up,
    moves.left: moves.down,
    moves.up: moves.right,
    moves.down: moves.left,
}

moves_map = {
    "/": {
        moves.right: [moves.up],
        moves.left: [moves.down],
        moves.up: [moves.right],
        moves.down: [moves.left],
    },
    "\\": {
        moves.right: [moves.down],
        moves.left: [moves.up],
        moves.up: [moves.left],
        moves.down: [moves.right],
    },
    "-": {
        moves.right: [moves.right],
        moves.left: [moves.left],
        moves.up: [moves.right, moves.left],
        moves.down: [moves.right, moves.left],
    },
    "|": {
        moves.right: [moves.up, moves.down],
        moves.left: [moves.up, moves.down],
        moves.up: [moves.up],
        moves.down: [moves.down],
    },
    ".": {
        moves.right: [moves.right],
        moves.left: [moves.left],
        moves.up: [moves.up],
        moves.down: [moves.down],
    },
}


def beam_move(position, direction):
    moves_stack = [(position, direction)]
    while moves_stack:
        current_position, current_direction = moves_stack.pop()
        if (
            current_position[0] < 0
            or current_position[0] >= len(input)
            or current_position[1] < 0
            or current_position[1] >= len(input[0])
            or beam_map[current_position[0]][current_position[1]].get(current_direction)
        ):
            continue
        beam_map[current_position[0]][current_position[1]][current_direction] = True
        current_tile = input[current_position[0]][current_position[1]]
        for move in moves_map.get(current_tile).get(current_direction):
            moves_stack.append(
                (tuple(current_position[i] + move[i] for i in range(2)), move)
            )


start_positions = []
for y in range(len(input[0])):
    start_positions.extend([((0, y), moves.down), ((len(input) - 1, y), moves.up)])
for x in range(len(input)):
    start_positions.extend(
        [((x, 0), moves.right), ((x, len(input[0]) - 1), moves.left)]
    )

all_energized_tiles = []
for start_position in start_positions:
    beam_map = [[{} for _ in range(len(input[0]))] for _ in range(len(input))]
    beam_move(*start_position)
    all_energized_tiles.append(
        sum([sum([True in tile.values() for tile in row]) for row in beam_map])
    )


print(max(all_energized_tiles))
