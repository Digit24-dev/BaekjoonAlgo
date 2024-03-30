# 참고 자료 : https://gingerkang.tistory.com/86

import sys

input = sys.stdin.readline

class Node():
    def __init__(self, item) -> None:
        self.item = item
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self, root :Node) -> None:
        self.root = root

    def insert(self, item):
        self.current_node = self.root           # 루트부터 탐색한다.
        while True:
            if item < self.current_node.item:   
                # 넣을 item값이 루트보다 작을 경우
                if self.current_node.left is not None:
                    # item 값이 cur node보다 작고, 현재 노드의 왼쪽에 데이터가 있을 경우
                    self.current_node = self.current_node.left
                else:
                    # 현재 노드의 왼족에 데이터가 없을 경우, 넣을 node를 삽입하고 종료한다
                    self.current_node.left = Node(item)
                    break
            else:
                # 넣을 item값이 루트보다 클 경우
                if self.current_node.right is not None:
                    # item 값이 cur node보다 크고, 현재 노드의 오른쪽에 데이터가 있을 경우
                    self.current_node = self.current_node.right
                else:
                    # 현재 노드의 오른쪽에 데이터가 없을 경우, 넣을 node를 삽입하고 종료한다
                    self.current_node.right = Node(item)
                    break
    
    def search(self, item):
        self.current_node = self.root
        while self.current_node:
            if item < self.current_node.item:
                self.current_node = self.current_node.left
            elif item > self.current_node.item:
                self.current_node = self.current_node.right
            else:
                return True
        return False
    
    def delete(self, item):
        # 삭제할 노드가 있는지 검사하고 없으면 False
        # 검사를 한 후에는 삭제할 노드가 current_node, 삭제할 노드의 부모 노드가 parent화
        is_search = False
        self.current_node = self.root
        self.parrent = self.root
        
        while self.current_node:
            if self.current_node.item == item:
                is_search = True
                break
            elif item < self.current_node.item:
                self.parrent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parrent = self.current_node
                self.current_node = self.current_node.right
        
        if is_search == False: return False

        # 삭제할 노드가 자식 노드를 갖고 있지 않을 경우
        if self.current_node.left == None and self.current_node.right == None:
            if item < self.parrent.item:
                self.parrent.left = None
            else:
                self.parrent.right = None
        
        # 삭제할 노드가 왼쪽 자식 노드를 가지고 있을 경우
        if self.current_node.left is not None and self.current_node.right is None:
            if item < self.current_node.item:
                self.parrent.left = self.current_node.left
            else:
                self.parrent.right = self.current_node.left

        # 삭제할 노드가 오른쪽 자식 노드를 가지고 있을 경우
        if self.current_node.left is None and self.current_node.right is not None:
            if item < self.current_node.item:
                self.parrent.left = self.current_node.right
            else:
                self.parrent.right = self.current_node.right

        # 삭제할 노드가 양쪽의 자식을 모두 가지고 있을 경우
        if self.current_node.left is not None and self.current_node.right is not None:
            self.change_node = self.current_node.right
            self.change_node_parrent = self.current_node.right
            
            while self.change_node.left is not None:
                self.change_node_parrent = self.change_node
                self.change_node = self.change_node.left
            
            if self.change_node.right is not None:
                self.change_node_parrent.left = self.change_node.right
            else:
                self.change_node_parrent.left = None
            
            if item < self.parrent.item:
                self.parrent.item = self.change_node
                self.change_node.right = self.change_node.right
                self.change_node.left = self.change_node.left
            else:
                self.parrent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right

        return True

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
