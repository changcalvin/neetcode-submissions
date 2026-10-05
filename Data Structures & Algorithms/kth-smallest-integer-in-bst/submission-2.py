# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        ## Iterative Inorder
        stack = []
        curr = root

        while curr or stack:
            # 一直往左走
            while curr:
                stack.append(curr)
                curr = curr.left

            # 当前最小的未访问节点
            curr = stack.pop()

            k -= 1
            if k == 0:
                return curr.val
            
            # 再处理右子树
            curr = curr.right

# Time: O(n) worst
# Space: O(h)