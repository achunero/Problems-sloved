def num_of_latern_fish(input,day):
    days=0
    while days < day:
        temp = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        for i in input:
            if i == 0:
                temp[6] = input[0]
                temp[8] = input[0]
            else:
                temp[i-1] = temp[i-1] + input[i]
        days += 1
        input = temp

    sum=0
    for key,value in input.items():
        sum+=value

    return sum

if __name__ == "__main__":
    with open('input.txt') as f:
        my_list = [x.rstrip() for x in f]
    nums=[]
    num_dict = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    for i in my_list[0]:
        if i != ',':
            nums.append(int(i))
            num_dict[int(i)] += 1

    solution_1 = num_of_latern_fish(num_dict,80)
    solution_2 = num_of_latern_fish(num_dict,256)
    print(solution_1,solution_2)