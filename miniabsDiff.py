arr = [3,8,-10,23,19,-4,-14,27]

diff = abs(arr[-1] - arr[0])
for i in range(1,len(arr)):
    if abs(arr[i] - arr[i-1]) < diff:
        diff = abs(arr[i] - arr[i-1])

ans = []
for i in range(1,len(arr)):
    if abs(arr[i] - arr[i-1]) == diff:
        ans.append(sorted([arr[i],arr[i-1]]))
print(ans)