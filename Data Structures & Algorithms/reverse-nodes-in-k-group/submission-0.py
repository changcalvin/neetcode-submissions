# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # 找到当前组第 k 个节点
            kth = self.getKth(groupPrev, k)

            # 不足 k 个，不反转
            if not kth:
                break

            # 下一组的第一个节点
            groupNext = kth.next

            # reverse 当前这一组
            prev = groupNext
            cur = groupPrev.next

            while cur != groupNext:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # 当前组原来的第一个节点
            # reverse 后会变成最后一个
            tmp = groupPrev.next

            # 前一部分接到 reverse 后的新头 kth
            groupPrev.next = kth

            # 下一轮从当前组的新尾巴开始
            groupPrev = tmp

        return dummy.next


    def getKth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1

        return cur

# Time: O(n)
# Space: O(1)