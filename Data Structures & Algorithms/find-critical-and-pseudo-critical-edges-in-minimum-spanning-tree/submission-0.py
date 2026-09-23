class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ## kruskal + union-find

        # V = n, E = len(edges)
        
        ## time:
            # sort: O(ElogE)
            # kruskal: O(E) * O(E)
        ## total: O(E^2)

        ## space:
            # indexed_edges: O(E)
            # parent: O(V)
            # rank = O(V)
        ## total: O(V + E)



        indexed_edges = []

        for i, (u, v, w) in enumerate(edges):
            indexed_edges.append((w, u, v, i))
        
        indexed_edges.sort() 

        
        def kruskal(skip_edge = -1, force_edge = -1):
            parent = list(range(n))
            rank = [0] * n
            
            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]

            def union(x, y):
                root_x = find(x)
                root_y = find(y)

                if root_x == root_y:
                    return False
                
                if rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                elif rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1
                return True
            

            total_weight = 0
            edges_used = 0

            if force_edge != -1:
                w, u, v, _ = indexed_edges[force_edge]

                if union(u, v):
                    total_weight += w
                    edges_used += 1
                
            for i, (w, u, v, original_index) in enumerate(indexed_edges):
                if i == skip_edge:
                    continue
                if i == force_edge:
                    continue
                if union(u, v):
                    total_weight += w
                    edges_used += 1

                    if edges_used == n - 1:
                        break
                
            if edges_used != n - 1:
                return float('inf')
            
            return total_weight
        
        
        
        base_weight = kruskal()

        critical = []
        pseudo_critical = []

        for i in range(len(indexed_edges)):
            w, u, v, original_index = indexed_edges[i]

            if kruskal(skip_edge = i) > base_weight:
                critical.append(original_index)
            elif kruskal(force_edge = i) == base_weight:
                pseudo_critical.append(original_index)
        
        return [critical, pseudo_critical]

