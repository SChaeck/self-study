import sys
from collections import deque

n, m = map(int, input().split())
man = 0
grid = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
bfs = deque()
for i in range(n):
    grid.append(list(sys.stdin.readline().rstrip()))
    for j in range(m):
        if grid[i][j] == 'I':
            bfs.append([j, i])

while(bfs):
    x, y = bfs.popleft()
    if grid[y][x] == 'X':
        continue
    elif grid[y][x] == 'P':
        man += 1
    
    for i in range(4):
        testX = x + dx[i]
        testY = y + dy[i]
        if testX < 0 or testX >= m or testY < 0 or testY >= n or grid[testY][testX] == 'X':
            continue
        bfs.append([testX, testY])
    grid[y][x] = 'X'

print(man if man > 0 else 'TT')