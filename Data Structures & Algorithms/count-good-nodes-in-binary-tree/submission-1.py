# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            # 空节点，没有 good node
            if not node:
                return 0

            # 当前节点是否是 good node
            good = 1 if node.val >= max_so_far else 0

            # 更新当前路径最大值
            new_max = max(max_so_far, node.val)

            # 当前 + 左子树 + 右子树
            return (
                good
                + dfs(node.left, new_max)
                + dfs(node.right, new_max)
            )

        return dfs(root, root.val)

# Time: O(n)
# Space: O(h)