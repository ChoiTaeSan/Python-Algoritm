class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, sets1, sets2):
        root1 = self.find(sets1)
        root2 = self.find(sets2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]: self.rank[root2] += 1

def kruskal(graph):
    mst = []
    edges = []
    for u in graph:
        for v, w in graph[u]:
            edges.append((w, u, v))
    edges.sort()
    ds = DisjointSet(sum([list(map(lambda x: x[1], graph[u])) for u in graph], []))
    for w, u, v in edges:
        if ds.find(u) != ds.find(v):
            mst.append((u, v, w))
            ds.union(u, v)
    return mst

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 3), ('E', 6)],
    'C': [('A', 3), ('F', 5)],
    'D': [('B', 3)],
    'E': [('B', 6), ('F', 2)],
    'F': [('C', 5), ('E', 2)]
}
result = kruskal(graph)
print("Minimum Spanning Tree:", result)
