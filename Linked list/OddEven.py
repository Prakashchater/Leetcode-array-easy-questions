# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# def oddEvenList(self, head):
#     odds = Node(0)
#     evens = Node(0)
#     oddsHead = odds
#     evensHead = evens
#     isOdd = True
#     while head:
#         if isOdd:
#             odds.next = head
#             odds = odds.next
#         else:
#             evens.next = head
#             evens = evens.next
#         isOdd = not isOdd
#         head = head.next
#     evens.next = None
#     odds.next = evensHead.next
#     return oddsHead.next



def oddEvenList(self, head):
    if head is None or head.next is None:
        return head

    odd_p = head
    even_p = head.next
    odd = odd_p
    even = even_p
    while even is not None:
        if even.next is not None:
            odd.next = even.next
        else:
            odd.next = even_p
            return odd_p
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_p
    return odd









