"""
def countInversion(arr):
    count = 0
    i = 0
    j = i + 1
    while i < len(arr)-1:
        if arr[i] > arr[j]:
            count += 1
        else:
            j += 1
    i += 1
    return count
"""
def mergeSort(arr, n):
    temp_arr = [0] * n
    return mergesort(arr, temp_arr, 0, n-1)

def mergesort(arr, temp_arr, l, r):
    count = 0
    if l < r:
        mid = (l + r) // 2
        count += mergesort(arr, temp_arr, l, mid)
        count += mergesort(arr, temp_arr, mid+1, r)
        count += merge(arr, temp_arr, l, mid, r)
    return count

def merge(arr, temp_arr, l, mid, r):
    i = l
    j = mid + 1
    k = l
    count = 0
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            count += (mid - i + 1)
            k += 1
            j += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    while j <= r:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    for loop_var in range(l, r+1):
        arr[loop_var] = temp_arr[loop_var]
    return count



if __name__ == '__main__':
    arr = [2, 4, 1, 3, 5]
    n = len(arr)
    print(mergeSort(arr, n))