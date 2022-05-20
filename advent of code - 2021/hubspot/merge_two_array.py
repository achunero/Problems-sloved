def merge_two_array(input1,input2,limit):
    n1 = len(input1)
    n2 = len(input2)
    i = j = 0
    output = []

    while i < n1 and j < n2:
        if input1[i] < input2[j]:
            output.append(input1[i])
            i+=1
        else:
            output.append(input2[j])
            j+=1

        if len(output) == limit:
            return output

    if i < n1:
        while len(output) != limit and i < n1:
            output.append(input1[i])
            i+=1

    if j < n2:
        while len(output) != limit and j < n2:
            output.append(input2[j])
            j+=1

    return output

num1 = [1, 3, 5]
num2 = [2, 6, 8,9,10]

ans = merge_two_array(num1,num2,6)

print(ans)

