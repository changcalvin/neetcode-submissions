class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ## DFS
        # 建立无向图 adjacency list
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):
            # 标记当前节点已经访问
            visited.add(node)

            # 访问所有相邻节点
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        count = 0

        # 必须检查所有节点，因为图可能不连通
        for node in range(n):
            if node not in visited:
                # 找到了一个新的 connected component
                count += 1
                # 把这个 component 中所有节点全部访问
                dfs(node)

        return count



        # 设 V = n，E = len(edges)

        # 建图：O(E)；DFS 中每个节点访问一次，每条边最多看两次：O(V + E)。
        # 所以：Time: O(V + E)

        # Adjacency list + visited + recursion stack：
        # Space: O(V + E)