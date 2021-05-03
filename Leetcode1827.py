def MiniOperation(nums):
    c = 0
    n = len(nums)
    for i in range(n-1):
        if nums[i] >= nums[i+1]:
            temp = abs(nums[i+1] - nums[i])
            c += temp + 1
            nums[i+1] += temp + 1
    return c

if __name__ == '__main__':
    nums = [1, 1, 1]
    print(MiniOperation(nums))