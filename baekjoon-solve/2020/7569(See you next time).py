import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())

tomato = [[[_ for _ in range(M)] for _ in range(N)] for _ in range(M)]
goto = deque()
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(M)]

for z in range(H):
    for y in range(N):
        tomato[z][y] = list(map(int, sys.stdin.readline().split()))
        for x in range(M):
            if tomato[z][y][x] == 1:
                goto.append((z, y, x))

if not goto: # 1이 없는 경우는 토마토가 모두 익지 못하는 상황
    print(-1)
    
while goto:
    z, y, x = goto.popleft()
    
    if not visited[z][y][x]:
        visited[z][y][x] = True
        if x - 1 >= 0 and tomato[z][y][x - 1] == 0 and visited[z][y][x - 1] == False: 
    