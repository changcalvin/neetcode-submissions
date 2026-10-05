# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ## 建立 hashmap
        inorder_index = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0

        def dfs(left, right):
            nonlocal pre_idx

            # 当前 inorder 区间为空
            if left > right:
                return None

            # preorder 下一个元素就是当前子树的 root
            root_val = preorder[pre_idx]
            pre_idx += 1

            root = TreeNode(root_val)

            # root 在 inorder 中的位置
            mid = inorder_index[root_val]

            # preorder 是 Root → Left → Right
            # 所以必须先构建左子树，再构建右子树
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)