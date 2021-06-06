def MergeTwoLL(head1, head2, a, b):
    p1 = head1
    p2 = head2
    i = 0
    j = 0
#Taking the first pointer to a
    while i != a-1:
        p1 = p1.next
        i += 1
#Taking the 2nd pointer to b
    while j != b:
        p1 = p1.next
        j += 1
#Connecting the end of the p1 in the list2
    p1.next = head2

#Keeping track of The list2 till the end
    while head2 is not None:
        head2 = head2.next

#When list2 reaches the end then connect the tail of the list2 to the p2.
    head2.next = p2.next

#Finally return the List
    return head1



