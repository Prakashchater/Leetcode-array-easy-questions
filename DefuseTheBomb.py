def defuse(arr, k):
    n = len(arr)
    res = [0] * n
    for i in range(n):
        if k > 0:
            total = 0
            for x in range(1, k+1):
                total += arr[(i+x) % n]
            res[i] = total
        elif k < 0:
            total = 0
            for x in range(1,-k+1):
                total += arr[(i-x) % n]
            res[i] = total
        else:
            res[i] = 0
    return res




if __name__ == '__main__':
    arr = [5, 7, 1, 4]
    k = 3
    print(defuse(arr,k))