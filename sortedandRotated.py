def reverse_(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def rotate(arr,k,n):
    k = k % n
    reverse_(arr, 0, n-k-1)
    reverse_(arr, n-k, n-1)
    reverse_(arr, 0, n-1)
    return arr

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    k = 10
    n = len(arr)
    left = 0
    right =len(arr) - 1
    print(rotate(arr,k,n))

