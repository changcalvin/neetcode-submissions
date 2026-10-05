# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        ## iterative

        cur = root

        while cur:
            # p、q 都更小 → 两个节点都在 left subtree
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left

            # p、q 都更大 → 两个节点都在 right subtree
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right

            else:
                # 出现分叉：
                # 1. p、q 分别位于左右两边
                # 2. 或 cur 本身就是 p / q
                # 当前节点就是 lowest common ancestor
                return cur
        
        # Time: O(h)
        # Space: O(1)
        