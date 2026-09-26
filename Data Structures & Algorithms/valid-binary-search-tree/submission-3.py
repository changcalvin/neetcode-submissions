# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, lower, upper):
            # Base case：走到空节点，说明这条路径没有违反 BST
            if not node:
                return True

            # 当前 node 必须严格位于祖先共同决定的范围内
            # 题目定义 BST 不允许 duplicate，所以使用 <= 和 >=
            if node.val <= lower or node.val >= upper:
                return False

            # Left subtree：
            # 原来的 lower 不变，upper 收紧为当前 node.val
            left_valid = dfs(node.left, lower, node.val)

            # Right subtree：
            # lower 收紧为当前 node.val，原来的 upper 不变
            right_valid = dfs(node.right, node.val, upper)

            return left_valid and right_valid

        # Root 一开始没有任何上下界限制
        return dfs(root, float("-inf"), float("inf"))


        # Time: O(n)
        # Space: O(h)

