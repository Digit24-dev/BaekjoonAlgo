import sys
input = sys.stdin.readline

V, E = map(int, input().split())
# graph = [[] for _ in range(V + 1)]
parents = [i for i in range(V + 1)]

edges = []

for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

total = 0
for edge in edges:
    c, u, v = edge

    if find_parent(parents, u) != find_parent(parents, v):
        union(parents, u, v)
        total += c
    
print(total)