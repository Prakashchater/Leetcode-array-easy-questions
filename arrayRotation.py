# Time :O(N)  space: O(1)
def swap(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotation(arr, k, n):
    k = k % n
    swap(arr, 0, k-1)
    print(arr)
    swap(arr, k, n-1)
    print(arr)
    swap(arr, 0, n-1)
    print(arr)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    n = len(arr)
    k = 4
    rotation(arr, k, n)
