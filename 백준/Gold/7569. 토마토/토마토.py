import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())

tomato_storage = [[] for _ in range(H)]
next_day_ripe = deque()
day_cnt = -1

for k in range(H):
    for i in range(N):
        tomato_storage[k].append(list(map(int, sys.stdin.readline().split())))
        for j, tomato in enumerate(tomato_storage[k][i]):
            if tomato == 1:
                next_day_ripe.append([k, i, j])

while next_day_ripe:
    day_cnt += 1
    this_day_ripe = next_day_ripe
    next_day_ripe = deque()
    while this_day_ripe:
        z, x, y = this_day_ripe.popleft()
        for dz, dx, dy in [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]:
            nz = z + dz
            nx = x + dx
            ny = y + dy
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and tomato_storage[nz][nx][ny] == 0:
                next_day_ripe.append([nz, nx, ny])
                tomato_storage[nz][nx][ny] = 1

for tomato_floor in tomato_storage:
    for tomato_list in tomato_floor:
        if 0 in tomato_list:
            print(-1)
            exit()

print(day_cnt)