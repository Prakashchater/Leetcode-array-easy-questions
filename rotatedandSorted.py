def RotatedAndSorted(arr, target):
    if not arr:
        return -1
    l = 0
    h = len(arr) - 1

    while l <= h:
        mid = (l + h) // 2
        if target == arr[mid]:
            return mid

        if arr[l] <= arr[mid]:
            if arr[l] <= target <= arr[mid]:
                h = mid - 1
            else:
                l = mid + 1
        else:
            if arr[mid] <= target <= arr[h]:
                l = mid + 1
            else:
                h = mid - 1
    return -1

if __name__ == '__main__':
    arr = [7, 6, 5, 4, 0, 1, 2, 3]
    target = 4
    print(RotatedAndSorted(arr, target))
