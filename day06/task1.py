import re
from functools import reduce

with open("input.txt", "r") as f:
    lines = [re.sub(r"\s+", " ", line.strip()) for line in f.readlines()]

times = [int(i) for i in lines[0].split(":")[1].strip().split()]
distances = [int(i) for i in lines[1].split(":")[1].strip().split()]
solutions = []
for time, distance in zip(times, distances):
    solutions_count = 0
    for i in range(time + 1):
        i_distance = i * (time - i)
        if i * (time - i) > distance:
            solutions_count += 1
    solutions.append(solutions_count)

print(reduce((lambda x, y: x * y), solutions))
