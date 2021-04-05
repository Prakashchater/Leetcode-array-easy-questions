def solution(arr):
    l = [i*i for i in arr]
    return sorted(l)



if __name__ == '__main__':
    arr = [-4,-1,0,3,10]
    print(solution(arr))