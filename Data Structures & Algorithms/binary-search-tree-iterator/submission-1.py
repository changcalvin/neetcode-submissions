# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.itr = 0
        self.stack = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.stack.append(node.val)
            dfs(node.right)
        
        dfs(root)

    def next(self) -> int:
        res = self.stack[self.itr]
        self.itr += 1
        return res

    def hasNext(self) -> bool:
        return self.itr < len(self.stack)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()