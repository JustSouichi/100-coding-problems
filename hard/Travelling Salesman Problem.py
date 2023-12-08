import sys

def travelling_salesman(graph, s):
    V = len(graph)
    dp = [[sys.maxsize for _ in range(V)] for _ in range(1 << V)]
    dp[1 << s][s] = 0

    for mask in range(1 << V):
        for u in range(V):
            if mask & (1 << u):
                for v in range(V):
                    if mask & (1 << v) and graph[u][v] > 0:
                        new_mask = mask ^ (1 << u)
                        dp[mask][u] = min(dp[mask][u], dp[new_mask][v] + graph[u][v])
    
    return min(dp[-1][u] + graph[u][s] for u in range(V) if dp[-1][u] < sys.maxsize and u != s)
