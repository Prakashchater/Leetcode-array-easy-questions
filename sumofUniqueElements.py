def sumUnique(arr):
    un = arr
    temp = 0
    for i in arr:
        if un.count(i) >= 1:
            temp += 1
    return sum(un)-temp

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    print(sumUnique(arr))