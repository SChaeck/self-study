import sys
import copy
from collections import deque

M, N = map(int, sys.stdin.readline().split())

day_cnt = -1
tomato_storage = []
next_day_ripe = deque()
for i in range(N):
    tomato_storage.append(list(map(int, sys.stdin.readline().split())))
    for j, tomato in enumerate(tomato_storage[i]):
        if tomato == 1:
            next_day_ripe.append([i, j])


step = [[1, 0], [-1, 0], [0, 1], [0, -1]]
while next_day_ripe:
    day_cnt += 1
    this_day_ripe = next_day_ripe
    next_day_ripe = deque()
    while this_day_ripe:
        x, y = this_day_ripe.popleft()
        for dx, dy in step:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and tomato_storage[nx][ny] == 0:
                next_day_ripe.append([nx, ny])
                tomato_storage[nx][ny] = 1 
                ### 중요! deque에 넣을 때 미리 익혀버려서 한 번 덱에 들어간 토마토가 또 들어가는 일이 없도록 하자. 이러한 중복만 막아도 시간 많이 줄일 수 있을 듯.


for tomato_list in tomato_storage:
    if 0 in tomato_list:
        print(-1)
        break
else:
    print(day_cnt)