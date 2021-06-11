# def nextGreater(self, head):
#     stack = []
#     res = []
#     while head:
#         while stack and stack[-1][1] < head.val:
#             res[stack.pop()[0]] = head.val
#         stack.append([len(res), head.val])
#         res.append(0)
#         head = head.next
#     return res

def nextGreater(self, head):
    ans = []
    stack = []
    index = 0
    while head is not None:
        ans.append(0)
        curr_val = head.val
        while stack and stack[-1][0] < curr_val:
            last_val = stack.pop()
            ans[last_val[1]] = curr_val
        stack.append((curr_val, index))
        index += 1
        head = head.next
    return ans
