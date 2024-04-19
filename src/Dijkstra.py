import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 3), ('E', 6)],
    'C': [('A', 3), ('F', 5)],
    'D': [('B', 3)],
    'E': [('B', 6), ('F', 2)],
    'F': [('C', 5), ('E', 2)]
}
distances = dijkstra(graph, 'A')
print("Shortest Paths from A:", distances)
