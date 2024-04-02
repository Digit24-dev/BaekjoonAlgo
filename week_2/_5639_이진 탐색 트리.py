import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

class Node():
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

def makeTree(preorder):
    if not preorder:
        return None
    
    root = Node(preorder[0])
    stack = [root]

    for value in preorder[1:]:
        node = Node(value)

        if value < stack[-1].item:
            stack[-1].left = node
            stack.append(node)
        else:
            while stack and stack[-1].item < value:
                last = stack.pop()
            last.right = node
            stack.append(node)
    return root

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.item)

preorder = []
for line in sys.stdin:
    preorder.append(int(line.strip()))

root = makeTree(preorder)
postorder_traversal(root)

# while True:
#     try:
#         N = int(input())
        
#         # No data 
#         if root is None:
#             root = Node(N, None, None)
#         else:
#             # find
#             curNode = root
#             while curNode:
#                 if N < curNode.item:
#                     prevNode, LR = curNode, 'L'
#                     curNode = root.left
#                 elif N > curNode.item:
#                     prevNode, LR = curNode, 'R'
#                     curNode = root.right

#                 if LR == 'R':
#                     prevNode.right = Node(N, None, None)
#                 elif LR == "L":
#                     prevNode.left = Node(N, None, None)
#         print(root)

#     except Exception as e:
#         print(e)
#         break

# print(root)
