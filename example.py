def student(start,end,query):
    c = 0
    for i in range(len(start)):
        if start[i] <= query and end[i] >= query:
            c += 1
    return c



if __name__ == '__main__':
    start = [1,2,3]
    end = [3,7,7]
    query = 4
    print(student(start,end,query))
