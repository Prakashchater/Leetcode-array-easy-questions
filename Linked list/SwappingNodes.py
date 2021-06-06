# Time: O(1)      Space: O(N)
def swappingNodes(head, k):
    ans = []
    curr = head
    while curr:
        ans.append(curr)
        curr = curr.next
    ans[k-1].val, ans[len(ans) - k].val = ans[len(ans) - k].val, ans[k-1].val
    return head

# Time: O(N)      Space: O(1)
def swappingNode(head, k):
    #   Find the length of the given Linked List
    n = 0
    curr = head
    while curr:
        n += 1
        curr = curr.next
    #   Now take an empty node
    start = end = None
    count = 0
    curr = head
    while curr:
        # If we search from the start
        if count == k - 1:
            start = curr    #Store the val of k in start

        # If we search node from the end
        if count == n - k:
            end = curr      #Store the val of k in end

        count += 1
        curr = curr.next

    #Swap the value of Start and End
    start.val, end.val = end.val, start.val
    return head
