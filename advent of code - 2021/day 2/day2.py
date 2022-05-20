def depth_calculation(file):
    dpth = 0
    for unit in file:
        if unit[0] == 'down':
            dpth += int(unit[1])
        elif unit[0] == 'up':
            dpth -= int(unit[1])
        else:
            print("invalid input")
            exit()
    return dpth


def new_depth_calculation(file):
    aim = 0
    dpth = 0

    for unit in file:
        if unit[0] == 'down':
            aim += int(unit[1])
        elif unit[0] == 'up':
            aim -= int(unit[1])
        elif unit[0] == 'forward':
            dpth += (aim * int(unit[1]))
    return dpth


if __name__ == "__main__":
    with open('input.txt') as f:
        my_list = [tuple(x.rstrip().split()) for x in f]
    forward = [int(i[1]) for i in my_list if 'forward' in i[0]]
    up_down = [i for i in my_list if not 'forward' in i[0]]
    depth = depth_calculation(up_down)

    # Problem 1 Solution
    print(sum(forward), depth, (sum(forward) * depth))

    # Problem 2 Solution
    depth_new = new_depth_calculation(my_list)
    print(depth_new * (sum(forward)))
