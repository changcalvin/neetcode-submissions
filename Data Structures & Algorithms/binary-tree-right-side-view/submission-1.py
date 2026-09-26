# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # Edge case：empty tree
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            # 固定当前层的 node 数量
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                # 正常把下一层 nodes 加入 queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                # 当前层最后一个 node = 最右边的 node
                if i == level_size - 1:
                    res.append(node.val)

        return res

        # Time: O(n)
        # Space: O(n)