class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ## Eulerian Path（欧拉路径） + DFS / Hierholzer’s Algorithm
        graph = defaultdict(list)
        # 倒序排序，方便 pop() 取字典序最小的机场
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        route = []

        def dfs(airport):
            # 把当前机场所有 outgoing edges 用完
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            # 没有路可以继续走时，再加入答案
            route.append(airport)
        dfs("JFK")

        # DFS 得到的是反过来的路线
        return route[::-1]

# E = number of tickets
# Time: O(E log E)
# Space: O(E)