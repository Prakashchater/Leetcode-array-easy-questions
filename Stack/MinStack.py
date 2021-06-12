class Stack:
    def __init__(self):
        self.s = []

    def push(self, x):
        currMin = self.getMin()
        if currMin == None or x < currMin:
            currMin = x
        return self.s.append((x, currMin))

    def pop(self):
        return self.s.pop()

    def top(self):
        if len(self.s) == 0:
            return None
        return self.s[len(self.s)-1][0]

    def getMin(self):
        if len(self.s) == 0:
            return None
        return self.s[len(self.s)-1][1]