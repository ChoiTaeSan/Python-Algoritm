import heapq

def prim(graph, start):
    mst, edges, visited = [], [(0, start, start)], set()
    while edges:
        weight, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))
            for to_next, weight in graph[to]:
                if to_next not in visited:
                    heapq.heappush(edges, (weight, to, to_next))
    return mst

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 3), ('E', 6)],
    'C': [('A', 3), ('F', 5)],
    'D': [('B', 3)],
    'E': [('B', 6), ('F', 2)],
    'F': [('C', 5), ('E', 2)]
}
result = prim(graph, 'A')
print("Minimum Spanning Tree:", result)
