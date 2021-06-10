class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def oddEvenList(self, head):
    odds = Node(0)
    evens = Node(0)
    oddsHead = odds
    evensHead = evens
    isOdd = True
    while head:
        if isOdd:
            odds.next = head
            odds = odds.next
        else:
            evens.next = head
            evens = evens.next
        isOdd = not isOdd
        head = head.next
    evens.next = None
    odds.next = evensHead.next
    return oddsHead.next