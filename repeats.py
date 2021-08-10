def find_repeats(input_str):
    output = []
    if len(input_str) < 3:
        return []
    repeat_len = 0
    for idx in range(1, len(input_str)):
        if input_str[idx] == input_str[idx - 1]:
            repeat_len += 1
        elif repeat_len >= 3:
            output.append((idx - repeat_len - 1, idx))
            repeat_len = 0
        else:
            repeat_len = 0
    if repeat_len > 0:
        output.append((idx - repeat_len, idx + 1))
    return output


test_str = "heeeeellllloooooo"
for repeat in find_repeats(test_str):
    print(repeat, test_str[repeat[0]: repeat[1]])


def find_combinations(input_str):
    intervals = find_repeats(input_str)
    outputs = []

    def check_combination(idx, sidx=0, curr_str=""):
        if idx == len(intervals):
            outputs.append(curr_str)
            return
        start, end = intervals[idx]
        curr_str = curr_str + input_str[sidx: start]
        # first case, no substitution
        check_combination(idx + 1,
                          end, curr_str + input_str[start: end])
        # 2nd case, substitute with 2 letters`
        check_combination(idx + 1, end, curr_str +
                          input_str[start] + input_str[start])
        # 3rd case, with only one letter
        check_combination(idx + 1, end, curr_str + input_str[start])
        return

    check_combination(0)
    return outputs


res = find_combinations("heeeeelllllllooooooo")
print(len(res), len(set(res)), res)
