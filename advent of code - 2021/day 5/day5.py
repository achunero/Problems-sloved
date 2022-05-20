# global set
unique = set()
duplicate = set()


def addtoset(x, y):
    if (x, y) not in unique:
        unique.add((x, y))
    else:
        duplicate.add((x, y))


def horizontal_vertical_vents(x1, x2, y1, y2):
    if x1 == x2:
        if y1 < y2:
            incy = 1
        elif y1 > y2:
            incy = -1

        for i in range(y1, y2 + incy, incy):
            addtoset(x1, i)

    if y1 == y2:
        if x1 < x2:
            incx = 1
        elif x1 > x2:
            incx = -1

        for j in range(x1, x2 + incx, incx):
            addtoset(j, y1)

def including_diagonals_for_vents(x1,x2,y1,y2):

    if abs(x1-x2) == abs(y1-y2):

        if x1 < x2:
            incx = 1
        else:
            incx = -1

        if y1 < y2:
            incy = 1
        else:
            incy = -1
        temp = y1
        for i in range(x1,x2+incx,incx):
            addtoset(i,temp)
            temp+=incy


if __name__ == "__main__":
    with open('input.txt') as f:
        my_list = [x.rstrip() for x in f]

    for value in my_list:
        num1, num2 = value.split('->')
        x1, y1 = num1.split(',')
        x2, y2 = num2.split(',')

        # Solution 1 and Solution 2
        #Comment the else part to get Solution 1

        if int(x1) == int(x2) or int(y1) == int(y2):
            horizontal_vertical_vents(int(x1), int(x2), int(y1), int(y2))
        else:
            including_diagonals_for_vents(int(x1), int(x2), int(y1), int(y2))


    print(len(unique), len(duplicate))

