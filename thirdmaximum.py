import sys
arr = [1,1,2]
if len(arr) < 3:
    print(max(arr))
else:
    m1 = arr[0]
    for i in arr:
        if i > m1:
            m1 = i
    m2 = m3 = -sys.maxsize
    for i in arr:
        if i > m2 and i < m1:
            m2 = i
    for i in arr:
        if i > m3 and i < m2:
            m3 = i
    print(m3)