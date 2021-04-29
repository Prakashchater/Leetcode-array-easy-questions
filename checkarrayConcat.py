def concate(arr, pieces):
    d = {}
    for p in pieces:
        d[p[0]] = p
        # print(p)
    idx = 0
    while idx < len(arr):
        if arr[idx] in d:
            piece = d[arr[idx]]
            for p in piece:
                if p != arr[idx]: return False
                else:
                    idx += 1
        else:
            return False
    return True


if __name__ == '__main__':
    arr = [91,4,64,78]
    pieces = [[78],[4,64],[91]]
    print(concate(arr, pieces))