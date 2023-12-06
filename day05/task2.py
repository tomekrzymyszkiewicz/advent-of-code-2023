with open("day05/input.txt", "r") as f:
    sections = f.read().split("\n\n")

seeds_numbers = [int(i) for i in sections[0].split(":")[1].strip().split()]
seeds = [
    (seeds_numbers[i], seeds_numbers[i] + seeds_numbers[i + 1])
    for i in range(0, len(seeds_numbers), 2)
]


maps = [
    [
        [int(i) for i in map_range.strip().split()]
        for map_range in section.splitlines()[1:]
    ]
    for section in sections[1:]
]


for ranges_map in maps:
    new = []
    while len(seeds) > 0:
        ss, se = seeds.pop()
        for a, b, c in ranges_map:
            os = max(ss, b)
            oe = min(se, b + c)
            if os < oe:
                new.append([os - b + a, oe - b + a])
                if os > ss:
                    seeds.append([ss, os])
                if se > oe:
                    seeds.append([oe, se])
                break
        else:
            new.append([ss, se])
    seeds = new

print(min([seed[0] for seed in seeds]))
