"""
def mergeInterval(arr):
    arr.sort()
    m = []
    s = -10000
    max = -100000
    for i in range(len(arr)):
        a = arr[i]
        if a[0] > max:
            if i != 0:
                m.append([s, max])
            max = a[1]
            s = a[0]
        else:
            if a[1] >= max:
                max = a[1]

    if max != -100000 and [s, max] not in m:
        m.append([s, max])
    print("The Merged Intervals are :", end=" ")
    for i in range(len(m)):
        print(m[i], end=" ")
"""
def mergeInterval(arr):
    arr.sort()
    m = []
    for i in arr:
        if not m or m[-1][-1] < i[0]:
            m.append(i)
        else:
            m[-1][-1] = max(m[-1][-1], i[1])
    return m



if __name__ == '__main__':
    arr = [[1,3],[15,18],[2,6],[8,10]]
    print(mergeInterval(arr))