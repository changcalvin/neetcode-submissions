# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
         
        ## DFS

        res = []

        def dfs(node, depth):
            # Base case
            if not node:
                return

            # 第一次到达这一层时，创建新的 list
            if depth == len(res):
                res.append([])

            # 当前 node 放入对应的 level
            res[depth].append(node.val)

            # 下一层 depth + 1
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return res

        # Time: O(n)
        # Space: O(h) recursion stack
        