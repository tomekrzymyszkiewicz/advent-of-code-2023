from skspatial.measurement import area_signed

with open("input.txt", "r") as f:
    moves = [[line.split(" ")[0], int(line.split(" ")[1])] for line in f.readlines()]


moves_dict = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

polygon = []
current_pos = [0, 0]
lenght_of_loop = 0
for direction, step in moves:
    lenght_of_loop += step
    polygon.append(
        current_pos := [
            current_pos[i] + moves_dict[direction][i] * step for i in range(2)
        ]
    )


print(int(area_signed(list(reversed(polygon))) + lenght_of_loop / 2 + 1))
