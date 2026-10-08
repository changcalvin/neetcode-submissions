# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        
        def dfs(node, curMax):
            if not node:
                return
            if node.val >= curMax:
                curMax = node.val
                self.res += 1
            dfs(node.left, curMax)
            dfs(node.right, curMax)
        
        dfs(root, float('-inf'))
        return self.res


            