# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # root 都没有了，不可能找到 subRoot
        if not root:
            return False

        # 当前节点作为起点，检查两棵树是否完全相同
        if self.sameTree(root, subRoot):
            return True

        # 当前不行，去左右子树继续寻找
        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

    def sameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return (
            self.sameTree(p.left, q.left)
            and self.sameTree(p.right, q.right)
        )