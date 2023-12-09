with open("input.txt", "r") as f:
    histories = [
        list(reversed(list(map(int, history.split())))) for history in f.read().strip().split("\n")
    ]


def get_differences(history: [int]) -> [int]:
    return [history[i + 1] - history[i] for i in range(len(history) - 1)]


def get_series(history: str) -> [[int]]:
    series = [history.copy()]
    current_differences = history
    while any([i != 0 for i in current_differences]):
        current_differences = get_differences(current_differences)
        series.append(current_differences)
    series[-1].append(0)
    return series


def get_prediction(history: str) -> int:
    series = get_series(history)
    for i in reversed(range(len(series) - 1)):
        series[i].append(series[i][-1] + series[i + 1][-1])
    return series[0]


print(sum([get_prediction(history)[-1] for history in histories]))
