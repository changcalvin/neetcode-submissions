"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = {}
        # 作用：
        # 1. visited：这个节点是不是已经访问/复制过
        # 2. mapping：原节点对应哪个新节点

        def dfs(curr):
            # 已经复制过，直接返回对应的新节点
            if curr in old_to_new:
                return old_to_new[curr]

            # 复制当前节点
            copy = Node(curr.val)
            # 一定要先加入 hashmap，再递归 neighbors
            old_to_new[curr] = copy

            # 递归复制所有邻居
            for neighbor in curr.neighbors:
                copied_neighbor = dfs(neighbor)
                copy.neighbors.append(copied_neighbor)

            return copy

        return dfs(node)

        ## time: O(V + E)
        ## space: O(V)
