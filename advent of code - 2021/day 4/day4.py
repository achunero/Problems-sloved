def checkbingo(input):
    for col in range(0,len(input)):
        colsum=0
        for row in range(0,len(input)):
            colsum += input[row][col]
            if sum(input[row]) == 5:
                return True
        if colsum == 5:
            return True
    return False

def find_sum_of_unmatched_number(bingo,matrix):
    sum=0
    for row in range(0,len(bingo)):
        if 0 in bingo[row]:
            for idx,val in enumerate(bingo[row]):
                if val == 0:
                    sum += matrix[row][idx]
    return sum

def process_scorecard(nums,matrix,prevcnt,res,solution):
    cnt = 0

    # The bingo matrix is a [0,1] matrix to track if we have a BINGO, loop until we hit a BINGO

    bingo = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    while not checkbingo(bingo):
        for row in range(0, len(matrix)):
            if nums[cnt] in matrix[row]:
                idx = matrix[row].index(nums[cnt])
                bingo[row][idx] = 1
        cnt += 1
    # Check if the prev count is less than current count for part 1 or greater for part
    # calculate the sum if not skip
    # and return the prev count

    if solution == 1:

        if (cnt-1) < prevcnt:
            prevcnt = cnt-1
            sequence_sum = find_sum_of_unmatched_number(bingo,matrix)
            res = sequence_sum*(nums[prevcnt])
        else:
            res = res
            prevcnt = prevcnt

    else:

        if (cnt-1) > prevcnt:
            prevcnt = cnt-1
            sequence_sum = find_sum_of_unmatched_number(bingo,matrix)
            res = sequence_sum*(nums[prevcnt])
        else:
            res = res
            prevcnt = prevcnt

    return (res,prevcnt)


if __name__ == "__main__":

    # Read the input file
    file = open("input.txt")

    # Parse the 1st line of file for the numbers
    nums = file.readline().rstrip().split(',')
    nums = list(map(int, nums))

    # A variable to track the lowest cnt and its respective result.
    prevcnt1 = len(nums)
    prevcnt2 = 0
    res1 = res2 = 0

    #Initial empty matrix
    mat = []
    print(nums)
    next(file)

    # Parsing through each line of the file and when it encounters a newline that means a 5X5 matrix is build and ready
    # for score card processing
    for line in file:
        if line != '\n':
            row = line.rstrip().split()
            row = list(map(int,row))
            mat.append(row)
        else:
            # Solution Part 1
            res1, prevcnt1 = process_scorecard(nums, mat, prevcnt1,res1,1)

            #Solution Part 2
            res2, prevcnt2 = process_scorecard(nums, mat, prevcnt2,res2,2)
            mat = []

    print(res1,prevcnt1)
    print(res2,prevcnt2)
