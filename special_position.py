def special_matrix(arr):
    n = len(arr)
    m = len(arr[0])
    lst = [[arr[j][i] for j in range(n)] for i in range(m)]
    print(lst)
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1 and sum(arr[i]) == 1 and sum(lst[j]) == 1:
                count += 1
    return count

if __name__ == '__main__':
    arr = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(special_matrix(arr))