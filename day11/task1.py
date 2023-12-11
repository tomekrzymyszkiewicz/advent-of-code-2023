with open("input.txt", "r") as f:
    galaxy_map = [[*line] for line in f.read().strip().splitlines()]


def expand_map(galaxy_map: list[list[str]]) -> list[str]:
    expanded_galaxy_map = []
    for row in galaxy_map:
        if not "#" in row:
            expanded_galaxy_map.append(row)
        expanded_galaxy_map.append(row)
    column = 0
    while column < len(expanded_galaxy_map[0]):
        if not "#" in [row[column] for row in expanded_galaxy_map]:
            for row in range(len(expanded_galaxy_map)):
                expanded_galaxy_map[row].insert(column, ".")
            column += 1
        column += 1
    return expanded_galaxy_map


def count_paths_to_other_nodes(
    galaxy_map: list[list[str]], node_i: int, node_j: int
) -> int:
    paths_length = 0
    for i in range(node_i, len(galaxy_map)):
        for j in range(len(galaxy_map[0])):
            if galaxy_map[i][j] == "#" and not (node_i == i and node_j == j):
                paths_length += abs(i - node_i) + abs(j - node_j)
    return paths_length, galaxy_map


def count_paths_lengths(galaxy_map: list[list[str]]) -> int:
    path_lengths = 0
    for i in range(len(galaxy_map)):
        for j in range(len(galaxy_map[0])):
            if galaxy_map[i][j] == "#":
                path_lengths_from_node, galaxy_map = count_paths_to_other_nodes(
                    galaxy_map, i, j
                )
                path_lengths += path_lengths_from_node
                galaxy_map[i][j] = "."
    return path_lengths


galaxy_map = expand_map(galaxy_map)
print(count_paths_lengths(galaxy_map))
