# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Tree -> String
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return

            res.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join(res)


    # String -> Tree
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        i = 0

        def dfs():
            nonlocal i

            if values[i] == "N":
                i += 1
                return None

            node = TreeNode(int(values[i]))
            i += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()