# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        stack = []
        res = 0
        while fast and fast.next:
            stack.append(slow)
            fast = fast.next.next
            slow = slow.next
        
        while stack:
            res = max(res, stack.pop().val + slow.val)
            slow = slow.next
            
        return res
            