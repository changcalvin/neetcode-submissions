class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
         # 建立无向图 adjacency list
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        # parent：当前 node 是从哪个节点过来的
        def dfs(node, parent):
            # 当前节点已经访问过 → 找到 cycle
            if node in visited:
                return False

            visited.add(node)

            for nei in graph[node]:
                # 无向图一定会看到刚刚来的 parent
                # 这不算 cycle，所以跳过
                if nei == parent:
                    continue

                if not dfs(nei, node):
                    return False

            return True

        # 条件 1：不能有 cycle
        if not dfs(0, -1):
            return False

        # 条件 2：所有 n 个节点必须 connected
        return len(visited) == n


        # V = n
        # E = len(edges)

        # 建 adjacency list：O(E)
        # DFS 每个 node 一次、每条 edge 最多看两次：O(V + E)
        # 所以：Time: O(V + E)
        
        # Adjacency list O(V + E) + visited O(V) + recursion stack O(V)：
        # Space: O(V + E)