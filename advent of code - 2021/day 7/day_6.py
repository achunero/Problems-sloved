from statistics import median

def find_fuel_count(input,n):
    sum = 0
    for i in input:
        sum = sum + (abs(i - n))

    return sum

def find_corrected_fuel_count(input,n):
    sum = 0
    for i in input:
        diff = abs(i - n)
        sum = sum + ((diff * (diff+1))/2)

    return sum

if __name__ == "__main__":
    with open('input.txt') as f:
        my_list = [x.rstrip() for x in f]
    nums=my_list[0].split(',')
    nums = list(map(int, nums))
    med = median(nums)
    mean = int(sum(nums)/len(nums))

    print(med,find_fuel_count(nums,int(med)))
    print(mean,find_corrected_fuel_count(nums,mean))
