from collections import deque

def topological_sort(graph):
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque([u for u in in_degree if in_degree[u] == 0])
    top_order = []

    while queue:
        u = queue.popleft()
        top_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(top_order) == len(in_degree):
        return top_order
    else:
        return None  # There is a cycle in the graph

graph = {
    'A': {'B', 'C'},
    'B': {'D'},
    'C': {'D'},
    'D': {'E'},
    'E': {}
}
result = topological_sort(graph)
print("Topological Sorting:", result)
