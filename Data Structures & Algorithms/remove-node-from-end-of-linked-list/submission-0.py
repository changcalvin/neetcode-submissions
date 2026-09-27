# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy 放在 head 前面，方便处理删除 head 的情况
        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        # fast 先走 n 步
        for _ in range(n):
            fast = fast.next

        # fast 到最后一个节点时，
        # slow 正好在待删除节点的前一个节点
        while fast.next:
            slow = slow.next
            fast = fast.next

        # 删除 slow 后面的节点
        slow.next = slow.next.next

        return dummy.next

        # Time: O(L)
        # Space: O(1)