# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(node):
            nonlocal res

            if not node:
                return 0

            # 负贡献直接不要
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # 当前 node 作为最高点，左右都可以取
            res = max(res, node.val + left + right)

            # 返回 parent 时只能选择一边
            return node.val + max(left, right)

        dfs(root)

        return res