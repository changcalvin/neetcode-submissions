# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # Edge case：empty tree
        if not root:
            return []

        res = []

        # BFS queue：保存接下来需要访问的 nodes
        queue = deque([root])

        while queue:
            
            level = []

            # 关键：进入这一层时先固定 node 数量
            # 后面加入 queue 的 children 属于下一层，不能在本轮处理
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                # 只把存在的 children 加入下一层
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            # 当前层处理完，再加入最终结果
            res.append(level)

        return res

        # Time: O(n)
        # Space: O(n)