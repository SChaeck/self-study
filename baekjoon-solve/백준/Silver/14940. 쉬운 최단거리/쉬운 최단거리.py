import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())

bfs_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
distance_map = [[0 for _ in range(m)] for _ in range(n)]
next_goto = deque()
distance = 1

loop_break = False
for y, bfs_list in enumerate(bfs_map):
    for x, target in enumerate(bfs_list):
        if target == 2:
            next_goto.append([x, y])
            bfs_map[y][x] = 0
            loop_break = True
            break
    if loop_break:
        break

while next_goto:
    goto = next_goto
    next_goto = deque()
    while goto:
        x, y = goto.popleft()
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n and bfs_map[ny][nx] != 0:
                next_goto.append([nx, ny])
                bfs_map[ny][nx] = 0
                distance_map[ny][nx] = distance
    distance += 1

for y, distance_list in enumerate(distance_map):
    for x, distance_ in enumerate(distance_list):
        if bfs_map[y][x] == 1:
            print(-1, end=' ')
        else:
            print(distance_, end=' ')
    print()