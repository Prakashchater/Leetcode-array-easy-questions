def rank(arr):
    sorted_arr = sorted(arr)
    rank = 1
    sorted_arr_rank = [1]

    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] != sorted_arr[i-1]:
            rank += 1
        sorted_arr_rank.append(rank)
    # print(sorted_arr_rank)
    r = []
    for num in arr:
        for key, val in enumerate(sorted_arr):
            if val == num:
                r.append(sorted_arr_rank[key])
                break
    return r






if __name__ == '__main__':
    arr = [40,10,30,10]
    print(rank(arr))

# a = [1,23,4,5,6,6]
# for i in enumerate(a):
#     print(i)
