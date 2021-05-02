def number(arr):
    seen = set()
    for i in arr:
        if 2 * i in seen or i / 2 in seen:
            return True
        seen.add(i)
    return False



if __name__ == '__main__':
    arr = [4,1,3,3]
    print(number(arr))