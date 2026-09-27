# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ## Iterative
        
        # prev：已经反转好的链表头
        prev = None

        # curr：当前正在处理的节点
        curr = head

        while curr:
            # 必须先保存下一个节点，否则反转后会丢失
            nxt = curr.next

            # 反转当前节点的 next 指针
            curr.next = prev

            # 两个指针向前移动
            prev = curr
            curr = nxt

        # 最终 prev 指向新的 head
        return prev

        ## Time: O(n)
        ## Space: O(1)