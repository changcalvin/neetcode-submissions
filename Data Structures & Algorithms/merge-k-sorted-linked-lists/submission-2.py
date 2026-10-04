# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # 每条链表先放第一个节点
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        tail = dummy

        while heap:
            # 当前所有链表头中最小的节点
            val, i, node = heapq.heappop(heap)

            # 接到结果链表
            tail.next = node
            tail = tail.next

            # 该链表继续往后走一个节点
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next

# N = 所有链表节点总数
# k = 链表数量

# Time: O(N log k)
# Space: O(k)，heap 最多存 k 个节点。