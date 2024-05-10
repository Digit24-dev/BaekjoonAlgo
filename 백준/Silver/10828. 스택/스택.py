import sys

class MyStack():
    def __init__(self) -> None:
        self.arr = []
        self.top = -1

    def push(self, n):
        self.arr.append(n)
        self.top = self.top + 1
        pass

    def tops(self):
        if self.top == -1:
            return -1
        else:
            return self.arr[self.top]
    
    def empty(self):
        if self.top == -1:
            return 1
        else:
            return 0
        
    def size(self):
        return self.top + 1
    
    def pop(self):
        ret = self.arr[self.top]
        self.arr.pop()
        self.top = self.top - 1
        return ret


N = int(sys.stdin.readline())
st = MyStack()

for _ in range(0, N):
    com = sys.stdin.readline().split()

    if com[0] == 'push':
        st.push(com[1])
    elif com[0] == 'pop':
        if st.empty():
            print(-1)
            continue
        print(st.pop())
    elif com[0] == 'top':
        print(st.tops())
    elif com[0] == 'size':
        print(st.size())
    elif com[0] == 'empty':
        print(st.empty())