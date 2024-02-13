from collections import deque
import sys

o = int(sys.stdin.readline())
que = deque()

for i in range(o) :
    ord = sys.stdin.readline().rstrip().split()
    if ord[0] == 'push' :
        que.append(ord[1])
    elif ord[0] == 'pop' :
        if que : print(que.popleft())
        else : print(-1)
    elif ord[0] == 'size' :
        print(len(que))
    elif ord[0] == 'empty' :
        if que : print(0) 
        else : print(1)
    elif ord[0] == 'front' :
        if que : print(que[0])
        else : print(-1)
    else :
        if que : print(que[-1])
        else : print(-1)