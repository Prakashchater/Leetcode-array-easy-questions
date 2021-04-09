def kadaneAlgo(arr):
    global_max = 0
    for i in range(len(arr)+1):
        for j in range(len(arr)+1):
            if arr[i:j]:
                current_max = sum(arr[i:j])
                # print(current_max, arr[i:j])
                if current_max > global_max:
                    global_max = current_max
    return global_max



if __name__ == '__main__':
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(kadaneAlgo(arr))