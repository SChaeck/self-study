import sys
from collections import deque

n = int(sys.stdin.readline()) # 노드의 수
e = int(sys.stdin.readline()) # 간선의 수
graph = [[] for _ in range(n)]
visited = [False for _ in range(n)]
bfs = deque()
count = 0

for _ in range(e):
    f, s = map(int, sys.stdin.readline().strip().split())
    graph[f-1].append(s-1)
    graph[s-1].append(f-1)

### BFS ###
bfs.append(0)

while(bfs):
    node = bfs.popleft()
    if visited[node]:
        continue
    for nn in graph[node]:
        bfs.append(nn)
    count += 1
    visited[node] = True


print(count-1)

