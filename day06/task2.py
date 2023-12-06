import re
from math import ceil, floor

with open("input.txt", "r") as f:
    lines = [re.sub(r"\s+", " ", line.strip()) for line in f.readlines()]

time = float("".join(lines[0].split(":")[1].strip().split()))
distance = float("".join(lines[1].split(":")[1].strip().split()))
min_solution = ceil((-time + ((time**2 - 4 * distance) ** 0.5)) / (-2))
max_soluition = floor((-time - ((time**2 - 4 * distance) ** 0.5)) / (-2))

print(max_soluition - min_solution + 1)
