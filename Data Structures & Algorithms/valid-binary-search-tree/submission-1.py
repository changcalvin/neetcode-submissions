# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        ## iterative

        # 每个元素同时保存 node 和它允许的范围
        stack = [(root, float("-inf"), float("inf"))]

        while stack:
            node, lower, upper = stack.pop()

            if not node:
                continue

            if node.val <= lower or node.val >= upper:
                return False

            # Right subtree 更新 lower
            stack.append((node.right, node.val, upper))

            # Left subtree 更新 upper
            stack.append((node.left, lower, node.val))

        return True
        