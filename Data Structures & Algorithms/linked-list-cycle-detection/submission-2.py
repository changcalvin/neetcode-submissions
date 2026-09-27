# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        ## Hash Set

        visited = set()
        curr = head

        while curr:

            if curr in visited:
                return True

            visited.add(curr)
            curr = curr.next

        return False

# 时间也是 O(n)，但空间是 O(n)。