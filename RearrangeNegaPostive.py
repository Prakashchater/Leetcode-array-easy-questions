# Time: O(N*log(N))       Space: O(1)
def rearrange(arr):
    arr.sort()
    i = 1
    j = 1
    while j < len(arr):
        if arr[j] > 0:
            break
        j += 1

    while arr[i] < 0 and j < len(arr):
        arr[i], arr[j] = arr[j], arr[i]
        i += 2
        j += 1
    return arr

if __name__ == '__main__':
    arr = [-5, 5, -2, 2, -8, 4, 7, 1, 8, 0]
    print(rearrange(arr))