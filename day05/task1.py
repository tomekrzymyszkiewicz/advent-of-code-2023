with open("day05/input.txt", "r") as f:
    sections = f.read().split("\n\n")


almanac = {}
parameters_names = []
for section in sections:
    section_name, section_content = section.split(":")
    match section_name:
        case "seeds":
            almanac[section_name] = [int(i) for i in section_content.strip().split()]
        case _:
            map_rules = [
                [int(i) for i in line.strip().split()]
                for line in section_content.strip().splitlines()
            ]
            destination_name = section_name.replace(" map", "").split("-to-")[1]
            parameters_names.append(destination_name)
            almanac[destination_name] = []
            for rule in map_rules:
                almanac[destination_name].append(
                    [rule[1], rule[1] + rule[2] - 1, rule[0] - rule[1]]
                )
seeds_parameters = {
    seed_value: {k: -1 for k in parameters_names} for seed_value in almanac["seeds"]
}


def get_parameter(rules: [[int]], source_value: int) -> int:
    for rule in rules:
        if rule[0] <= source_value <= rule[1]:
            return source_value + rule[2]
    return source_value


for seed_number, parameters in seeds_parameters.items():
    seeds_parameters[seed_number][parameters_names[0]] = get_parameter(
        rules=almanac.get(parameters_names[0]), source_value=seed_number
    )

    for i in range(1, len(parameters)):
        seeds_parameters[seed_number][parameters_names[i]] = get_parameter(
            rules=almanac.get(parameters_names[i]),
            source_value=seeds_parameters[seed_number].get(parameters_names[i - 1]),
        )

print(
    min(
        seeds_parameters.get(seed_number).get("location")
        for seed_number in almanac.get("seeds")
    )
)
