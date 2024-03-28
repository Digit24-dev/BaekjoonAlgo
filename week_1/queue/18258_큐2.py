import sys
from queue import Queue
from collections import deque

class MyQueue:
    def __init__(self) -> None:
        self.arr = []
        self.qsize = 0

    def empty(self):
        if self.qsize == 0:
            return 1
        else : return 0

    def front(self):
        if self.empty(): return -1
        else : return self.arr[0]

    def back(self):
        if self.empty(): return -1
        else : return self.arr[self.qsize - 1]

    def size(self):
        return self.qsize
    
    def push(self, item):
        self.qsize += 1
        self.arr.append(item)
        pass

    def pop(self):
        if self.empty(): return -1
        else :
            self.qsize -= 1
            return self.arr.pop(0)
        
N = int(input())
# arr = MyQueue()
# arr = Queue()

queue = []
qsize = [0]

def front():
    if qsize[0] == 0:
        print(-1)
    else:
        print(queue[0])
def back():
    if qsize[0] == 0:
        print(-1)
    else:
        print(queue[len(queue)-1])
def empty():
    if qsize[0] == 0: print(1)
    else: print(0)
def size():
    print(qsize[0])
def pop():
    if qsize[0] == 0: print(-1)
    else:
        print(queue[0])
        queue.pop(0)
        qsize[0] -= 1
def push(item):
        queue.append(item)
        qsize[0] += 1

command_dic = {
    "front": front,
    "back": back,
    "empty": empty,
    "size": size,
    "pop": pop,
    "push": push
    }

for _ in range(N):
    command = sys.stdin.readline().strip().split()
    if len(command) > 1:
        command_dic[command[0]](command[1])
    else:
        command_dic[command[0]]()

    # if command == "front":
    #     if qsize == 0:
    #         print(-1)
    #     else:
    #         print(queue[0])

    # elif command == "back":
    #     if qsize == 0:
    #         print(-1)
    #     else:
    #         print(queue[len(queue)-1])

    # elif command == "empty":
    #     if qsize == 0: print(1)
    #     else: print(0)

    # elif command == "size":
    #     print(qsize)

    # elif command == "pop":
    #     if qsize == 0: print(-1)
    #     else:
    #         print(queue[0])
    #         queue.pop(0)
    #         qsize -= 1

    # else:
    #     dat = command.split()
    #     qsize += 1
    #     queue.append(int(ord[1]))