def depth_of_measurements(input):
    prev = 0
    cnt = -1
    for line in input:
        if line > prev:
            cnt += 1
        prev = line
    return cnt


def depth_of_measuements_sliding_window(input, window):
    i = 0
    cnt = -1
    prev = 0
    while (i + window) < len(input)+1:
        if sum(input[i:(i + window)]) > prev:
            cnt += 1
        prev = sum(input[i:(i + window)])
        i += 1
    return cnt


if __name__ == "__main__":
    with open('input.txt') as f:
        my_list = [int(x.rstrip()) for x in f]
    depth = depth_of_measurements(my_list)
    sliding_depth = depth_of_measuements_sliding_window(my_list, 3)
    print(depth,sliding_depth)
