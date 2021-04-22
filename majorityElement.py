# def majority_element(nums):
#     majority_count = len(nums) // 2
#     for num in nums:
#         count = sum(1 for elem in nums if elem == num)
#         if count > majority_count:
#             return num
#
#
# if __name__ == '__main__':
#     nums = [1,1,2,2,2,1,1]
#     print(majority_element(nums))

def majority(nums):
    n = len(nums) // 2
    count = 0
    for num in nums:
        for ele in nums:
            if ele == num:
                count += 1
            if count > n:
                return num

if __name__ == '__main__':
    nums = [1,1,2,2,2,1,1]
    print(majority(nums))

