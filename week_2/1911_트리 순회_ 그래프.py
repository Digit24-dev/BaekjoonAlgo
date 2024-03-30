import sys

input = sys.stdin.readline

N = int(input())
g = dict()

for _ in range(N):
    node, left, right = map(str, input().split())
    g[node] = [left, right]

def preorder(root):
    if root == '.':
        return
    print(root, end='')
    preorder(g[root][0])
    preorder(g[root][1])


def inorder(root):
    if root == '.':
        return
    
    inorder(g[root][0])
    print(root, end='')
    inorder(g[root][0])


def postorder(root):
    if root == '.':
        return
    
    postorder(g[root][0])
    postorder(g[root][1])
    print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
