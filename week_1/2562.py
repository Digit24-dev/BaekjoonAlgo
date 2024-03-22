import sys

max = 0 
indexNum = 0

for i in range(1, 10):
    curN = int(sys.stdin.readline())
    
    if curN > max:
        max = curN
        indexNum = i
    
print(max)
print(indexNum)   
