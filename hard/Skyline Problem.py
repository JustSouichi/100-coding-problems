import heapq

def get_skyline(buildings):
    events = [(L, -H, R) for L, R, H in buildings]
    events += list(set((R, 0, 0) for _, R, _ in buildings))
    events.sort()

    res = [[0, 0]]
    heap = [(0, float("inf"))]
    for x, negH, R in events:
        while x >= heap[0][1]:
            heapq.heappop(heap)
        if negH:
            heapq.heappush(heap, (negH, R))
        if res[-1][1] != -heap[0][0]:
            res.append([x, -heap[0][0]])

    return res[1:]
