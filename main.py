# def oddidx(arr):
#     idx = []
#     for i in range(len(arr)):
#         if i < len(arr):
#             idx.append([arr[i]])
#         if i+2 < len(arr):
#             idx.append([arr[i:i+3]])
#     idx.append([arr[0:len(arr)]])
#     return idx
#
# if __name__ == '__main__':
#     arr = [1,2,3,4,5]
#     print(oddidx(arr))

def sumOddLengthSubarrays(arr):
    total, upper = 0, len(arr) - 1
    while upper >= 0:
        curr_upper, curr_lower = upper, 0
        while curr_upper < len(arr):
            slice = arr[curr_lower:curr_upper + 1]
            total += sum(slice) if len(slice) % 2 != 0 else 0
            curr_lower += 1
            curr_upper += 1
        upper -= 1
    return total

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    print(sumOddLengthSubarrays(arr))