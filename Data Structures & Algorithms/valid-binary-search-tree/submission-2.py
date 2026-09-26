# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        prev = float("-inf")

        def inorder(node):
            nonlocal prev

            # Base case
            if not node:
                return True

            # Left
            if not inorder(node.left):
                return False

            # 当前值必须严格大于 inorder 中前一个值
            if node.val <= prev:
                return False

            # 更新前一个访问的值
            prev = node.val

            # Right
            return inorder(node.right)

        return inorder(root)

        # Time: O(n)
        # Space: O(h)