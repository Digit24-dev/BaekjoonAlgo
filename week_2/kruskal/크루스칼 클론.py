import sys
input = sys.stdin.readline

v, e = map(int, input().split())

parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    else: return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges = []
total_cost = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for i in range(e):
    c, u, v = edges[i]
    
    if find_parent(parent, u) != find_parent(parent, v):
        union(parent, u, v)
        total_cost += c

print(total_cost)
