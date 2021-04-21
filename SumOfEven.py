def evnspecial(arr,qu):
    res = []
    Sum = sum(x for x in arr if x%2==0)
    # print(Sum)
    for val, idx in qu:
        if arr[idx] % 2 == 0: Sum -= arr[idx]
        arr[idx] += val

        if arr[idx] % 2 == 0: Sum += arr[idx]
        res.append(Sum)
    return res


if __name__ == '__main__':
    arr = [1,2,3,4,5]
    qu = [[1,0],[-3,1],[-4,0],[2,3]]
    print(evnspecial(arr,qu))



