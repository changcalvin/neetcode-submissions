# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = head

        # fast 要走两步，所以必须保证 fast 和 fast.next 都存在
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            # 两个指针指向同一个节点 → 存在环
            if slow == fast:
                return True

        # fast 能走到 None → 没有环
        return False
    
    ## Time: O(n)
    ## Space: O(1)