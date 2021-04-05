arr = [1,2,3,4,5]
"""
l = [[]]
for i in range(len(arr)+1):
    for j in range(i+1, len(arr)+1):
        temp = arr[i:j]
        l.append(temp)
print(l, end=" ")


count = 0
for i in range(len(arr)):
    for j in range(i,len(arr),2):
        for k in range(i,j+1, 1):
            count += arr[k]
print(count)

def sumOddLengthSubarrays(arr):
    count = 0
    for i in range(1, len(arr) + 1, 2):
        start = 0
        while start + i <= len(arr):
            count += sum(arr[start:start + i])
            start += 1
    return count

if __name__ == '__main__':
    arr = [1,2,3]
    print(sumOddLengthSubarrays(arr))
"""
# EVEN SUB-ARRAY LIST

