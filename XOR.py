xor = 0
out = []
arr = [10,11,1,2,3]
n = arr[len(arr)-1]
for i in range(len(arr)-1):
    out.append(arr[i]^arr[i+1])
out.append(arr[len(arr)-1])
print(out)