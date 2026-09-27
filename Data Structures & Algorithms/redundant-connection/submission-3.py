class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        # 一开始每个节点自己属于一个集合
        parent = list(range(n + 1))

        # rank 表示树的高度
        rank = [0] * (n + 1)

        # 找到 node 所属集合的 root
        def find(node):
            # Path Compression
            if parent[node] != node:
                parent[node] = find(parent[node])

            return parent[node]

        # 尝试连接 a 和 b
        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            # 已经属于同一个集合
            # 再连就会形成 cycle
            if rootA == rootB:
                return False

            # Union by Rank：矮树接到高树下面
            if rank[rootA] < rank[rootB]:
                parent[rootA] = rootB

            elif rank[rootA] > rank[rootB]:
                parent[rootB] = rootA

            else:
                # 一样高，任选一个作为 root
                parent[rootB] = rootA
                rank[rootA] += 1

            return True

        # 按输入顺序加入每条 edge
        for a, b in edges:
            if not union(a, b):
                return [a, b]

        ## Time: O(n α(n)) ≈ O(n)
        # parent + rank：
        # Space: O(n)