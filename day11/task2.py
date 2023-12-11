with open("input.txt", "r") as f:
    galaxy_map = [[*line] for line in f.read().strip().splitlines()]

empty_space_dist = 1_000_000


def empty_columns(galaxy_map: list[list[str]]) -> list[int]:
    empty_columns_list = []
    for i in range(len(galaxy_map[0])):
        if not "#" in [row[i] for row in galaxy_map]:
            empty_columns_list.append(i)
    return set(empty_columns_list)


def empty_rows(galaxy_map: list[list[str]]) -> list[int]:
    empty_rows_list = []
    for i in range(len(galaxy_map)):
        if not "#" in galaxy_map[i]:
            empty_rows_list.append(i)
    return set(empty_rows_list)


def count_paths_to_other_nodes(
    galaxy_map: list[list[str]],
    node_i: int,
    node_j: int,
    empty_rows_set: list,
    empty_columns_set: set,
) -> int:
    paths_length = 0
    for i in range(node_i, len(galaxy_map)):
        for j in range(len(galaxy_map[0])):
            if galaxy_map[i][j] == "#" and not (node_i == i and node_j == j):
                min_i, max_i = min(node_i, i + 1), max(node_i, i + 1)
                min_j, max_j = min(node_j, j + 1), max(node_j, j + 1)
                count_empty_rows = len(set(range(min_i, max_i)) & empty_rows_set)
                count_empty_columns = len(set(range(min_j, max_j)) & empty_columns_set)
                paths_length += (
                    abs(i - node_i)
                    + abs(j - node_j)
                    + (empty_space_dist - 1) * (count_empty_rows + count_empty_columns)
                )
    return paths_length, galaxy_map


def count_paths_lengths(galaxy_map: list[list[str]]) -> int:
    empty_columns_set = empty_columns(galaxy_map)
    empty_rows_set = empty_rows(galaxy_map)
    path_lengths = 0
    for i in range(len(galaxy_map)):
        for j in range(len(galaxy_map[0])):
            if galaxy_map[i][j] == "#":
                path_lengths_from_node, galaxy_map = count_paths_to_other_nodes(
                    galaxy_map, i, j, empty_rows_set, empty_columns_set
                )
                path_lengths += path_lengths_from_node
                galaxy_map[i][j] = "."
    return path_lengths


print(count_paths_lengths(galaxy_map))
