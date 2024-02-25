import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]
visited = [False for _ in range(N)]
cc_cnt = 0
# goto = deque()
goto = []

for _ in range(M):
    e1, e2 = map(int, sys.stdin.readline().split())
    graph[e1-1].append(e2-1)
    graph[e2-1].append(e1-1)

for index, v in enumerate(visited):
    if v == True:
        continue
    for e2 in graph[index]:
        goto.append(e2)    
    while goto:
        e2 = goto.pop()
        visited[e2] = True
        for e1 in graph[e2]:
            if visited[e1] == False:
                goto.append(e1)
    cc_cnt += 1

print(cc_cnt)