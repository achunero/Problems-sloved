def power_consumption_rate(input):
    gamma = epsilon = ''
    for i in range(0,len(input[0])):
        binary_numbers = []
        j=0
        while j < len(input):
            binary_numbers.append(input[j][i])
            j+=1

        if binary_numbers.count('1') > binary_numbers.count('0'):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return (int(gamma,2),int(epsilon,2))


def life_support_rating(input,type):
    i = 0
    while len(input) != 1:
        # A hash map to store the index value of the binary

        binary_dict = {'0':[],'1':[]}
        for indx,binary in enumerate(input):
            binary_dict[binary[i]].append(indx)
        tmp=[]

        # A type variable for O2 and CO2 rates, O2 will always reduce the input list with most occured bit binary value
        # and Co2 the opposite, reduce input list with the least occuring bit binary values
        if type == 'o2':

            if len(binary_dict['1']) >= len(binary_dict['0']):
                for idx in binary_dict['1']:
                    tmp.append(input[idx])
            else:
                for idx in binary_dict['0']:
                    tmp.append(input[idx])
        elif type == 'co2':
            if len(binary_dict['0']) =< len(binary_dict['1']):
                for idx in binary_dict['0']:
                    tmp.append(input[idx])
            else:
                for idx in binary_dict['1']:
                    tmp.append(input[idx])
        else:
            print("Type Error")
            exit()

        input = tmp
        i+=1
    return int(input[0],2)


if __name__ == "__main__":
    with open('input.txt') as f:
        my_list = [x.rstrip() for x in f]
    print(my_list)

    #Solution 1
    rate1,rate2 = power_consumption_rate(my_list)
    print(rate1,rate2, rate1*rate2)

    #Solution 2
    o2_rate = life_support_rating(my_list,'o2')
    co2_rate = life_support_rating(my_list,'co2')
    print(o2_rate,co2_rate,o2_rate*co2_rate)