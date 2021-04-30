from collections import Counter
def PairSocks(arr):
    l = []
    a = Counter(arr)
    # print(a)
    for num in a.values():
        temp = num // 2
        # print(temp)
        l.append(temp)
    return sum(l)

if __name__ =='__main__':
    arr = [10,20,20,10,10,30,50,10,20,20]
    print(PairSocks(arr))