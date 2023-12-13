with open("input.txt", "r") as f:
    patterns = [pattern.splitlines() for pattern in f.read().strip().split("\n\n")]


def vertical_reflection(pattern: list[str]) -> int:
    for left_spacing in range(len(pattern[0]) - 1):
        smuge_count = 0
        if left_spacing < len(pattern[0]) // 2:
            for i in range(left_spacing, -1, -1):
                left_col_index = i
                right_col_index = 2 * left_spacing - i + 1
                for j in range(len(pattern)):
                    if pattern[j][left_col_index] != pattern[j][right_col_index]:
                        smuge_count += 1
                    if smuge_count > 1:
                        break
            if smuge_count == 1:
                return left_spacing + 1
        else:
            for i in range(left_spacing, len(pattern[0]) - 1):
                left_col_index = 2 * left_spacing - i
                right_col_index = i + 1
                for j in range(len(pattern)):
                    if pattern[j][left_col_index] != pattern[j][right_col_index]:
                        smuge_count += 1
                        if smuge_count > 1:
                            break
            if smuge_count == 1:
                return left_spacing + 1
    return 0


def horizontal_reflection(pattern: list[str]) -> int:
    for top_spacing in range(len(pattern) - 1):
        smuge_count = 0
        if top_spacing < len(pattern) // 2:
            for i in range(top_spacing, -1, -1):
                top_row_index = i
                bottom_row_index = 2 * top_spacing - i + 1
                for j in range(len(pattern[0])):
                    if pattern[top_row_index][j] != pattern[bottom_row_index][j]:
                        smuge_count += 1
                        if smuge_count > 1:
                            break
            if smuge_count == 1:
                return top_spacing + 1
        else:
            for i in range(top_spacing, len(pattern) - 1):
                top_row_index = 2 * top_spacing - i
                bottom_row_index = i + 1
                for j in range(len(pattern[0])):
                    if pattern[top_row_index][j] != pattern[bottom_row_index][j]:
                        smuge_count += 1
                        if smuge_count > 1:
                            break
            if smuge_count == 1:
                return top_spacing + 1
    return 0


reflections_sum = sum(
    [
        100 * horizontal_reflection(pattern) + vertical_reflection(pattern)
        for pattern in patterns
    ]
)
print(reflections_sum)
assert reflections_sum == 33183