# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def dfs(node, depth):
            # Base case
            if not node:
                return

            # 第一次到达这一层：
            # 因为先走 right，所以当前 node 是这一层最右边的
            if depth == len(res):
                res.append(node.val)

            # 关键：必须先 right，再 left
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res

        # Time: O(n)
        # Space: O(h)
        