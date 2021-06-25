def buyAndSell(arr):
    profit = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            profit += arr[i] - arr[i-1]
    return profit

if __name__ == '__main__':
    arr = [100, 30, 15, 10, 8, 25, 80]
    print(buyAndSell(arr))