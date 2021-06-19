# time : O(N^2)   ||  Space: O(1)
# def twoSum(arr, target):
#     res = {}
#     for i in range(len(arr)-1):
#         first_num = arr[i]
#         for j in range(i+1, len(arr)):
#             second_num = arr[j]
#             current_sum = arr[i] + arr[j]
#             if target == current_sum:
#                 return [i, j, [first_num, second_num]]
#     return []


# time: O(N)    ||      Space: O(N)
# def twoSum(arr, target):
#     nums = {}
#     for i in arr:
#         pot_match = target - i
#         if pot_match in nums:
#             return [pot_match, i]
#         else:
#             nums[i] = True
#     return []



def twoSum(arr, target):
    arr.sort()
    left = 0
    right = len(arr)-1
    while left < right:
        current_sum = arr[left] + arr[right]
        if target == current_sum:
            return [left, right, [arr[left], arr[right]]]
        elif target < current_sum:
            right -= 1
        elif target > current_sum:
            left += 1
    return []

if __name__ == '__main__':
    arr = [1, 1, 1, 1]
    target = 2
    print(twoSum(arr, target))
