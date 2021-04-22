def occurance(arr):
    max_count = None
    count = 0
    res = {}

    for num in arr:
        if num not in res:
            res[num] = 1
        else:
            res[num] += 1
        if res[num] > count:
            count = res[num]
        max_count = num

    return max_count

if __name__ == '__main__':
    arr = [1,1,2,2,3,3,4,4,4,5,5,2,2,1,1,3,3,4,2,1,2,3,2,1,3,2]
    print(occurance(arr))