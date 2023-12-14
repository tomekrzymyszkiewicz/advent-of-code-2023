with open("input.txt", "r") as f:
    rocks = f.read().strip().splitlines()
rock_cols = [[rocks[j][i] for j in range(len(rocks))] for i in range(len(rocks[0]))]


def cubes_positions(rock_col: list[str]) -> list[int]:
    cubes_pos = [0]
    for i, rock in enumerate(rock_col):
        if rock == "#":
            cubes_pos.append(i)
    return cubes_pos


def rock_column_weights(rock_column: str):
    i = len(rock_column)
    while len(rock_column):
        try:
            next_cube_rock = rock_column.index("#")
            substring, rock_column = (
                rock_column[:next_cube_rock],
                rock_column[next_cube_rock + 1 :],
            )
        except:
            substring, rock_column = rock_column, []
        weight = sum(range(i - substring.count("O") + 1, i + 1))
        i -= len(substring) + 1
        yield weight


print(sum([sum(rock_column_weights(rock_col)) for rock_col in rock_cols]))
