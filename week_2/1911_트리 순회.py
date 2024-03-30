import sys

input = sys.stdin.readline

N = int(input())
# g = [[None] * N for _ in range(N)]

class Node:
    def __init__(self, item, left, right) -> None:
        self.item = item
        self.left = left
        self.right = right

g = {}

for i in range(N):
    node, left, right = map(str, input().split())
    g[node] = Node(item=node, left=left, right=right)


def preorder_dfs(node:Node):
    print(node.item, end='')
    if node.left != '.':
        preorder_dfs(g[node.left])
    if node.right != '.':
        preorder_dfs(g[node.right])


def postorder_dfs(node):
    if node.left != '.':
        postorder_dfs(g[node.left])
    if node.right != '.':
        postorder_dfs(g[node.right])
    print(node.item, end='')


def inorder_dfs(node):
    if node.left != '.':
        postorder_dfs(g[node.left])
    print(node.item, end='')
    if node.right != '.':
        postorder_dfs(g[node.right])

preorder_dfs(g['A'])
print()
inorder_dfs(g['A'])
print()
postorder_dfs(g['A'])
