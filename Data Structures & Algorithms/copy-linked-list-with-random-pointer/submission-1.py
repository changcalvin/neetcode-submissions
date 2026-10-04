"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # old node -> copied node
        old_to_new = {None: None}

        # Step 1: 创建所有新节点
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        # Step 2: 设置 next 和 random
        cur = head
        while cur:
            copy = old_to_new[cur]

            copy.next = old_to_new[cur.next]
            copy.random = old_to_new[cur.random]

            cur = cur.next

        return old_to_new[head]