# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ## Recursive
        
        # 空链表 / 已经到最后一个节点
        if not head or not head.next:
            return head

        # 先反转 head 后面的链表
        new_head = self.reverseList(head.next)

        # 原来的下一个节点反过来指向自己
        head.next.next = head

        # 断掉原来的连接
        head.next = None

        return new_head