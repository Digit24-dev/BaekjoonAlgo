# 참고 자료 : https://gingerkang.tistory.com/86

import sys

input = sys.stdin.readline

class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None
    
    # 노드 생성과 삽입
    def _insert_value(self, node :Node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    # 노드 탐색
    def find(self, key):
        return self._find_value(self.root, key)
    
    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted
    
    def _delete_value(self, node :Node, key):
        if node is None:
            return node, False
        
        deleted = False
        # 해당 노드가 삭제할 노드일 경우
        if key == node.data:
            deleted = True
            # 삭제할 노드가 자식이 두개일 경우
            if node.left and node.right:
                # 오른쪽 서브 트리에서 가장 왼쪽에 있는 노드를 찾고 교체
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            # 자식 노드가 하나일 경우 해당 노드와 교체
            elif node.left or node.right:
                node = node.left or node.right
            # 자식 노드가 없을 경우 그냥 삭제
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted


'''
이진 탐색 트리의 구현
1. 특징
  - 왼쪽 노드는 루트 노드보다 작고 오른쪽 노드는 루트 노드보다 크다.

2. 필요한 구현
  - 삽입
  - 삭제
  - 탐색

3. 배열의 위치?
  - 
'''

root = Node(30)
bst = BinarySearchTree(root=root)

arr = [1,2,3,4,5,6,7,8,9,10]

for i in arr:
    bst.insert(i)

s = [1,3,4,8,9,7,55,998,444]

for i in s:
    print(bst.search(i))
