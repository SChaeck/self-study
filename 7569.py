import sys

M, N, H = map(int, sys.stdin.readline().split())

tomato = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
goto = []
visited = {}

def check():
    mOne = False
    one = False
    zero = False
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if tomato[z][y][x] == 0:
                    zero = True
                if tomato[z][y][x] == -1:
                    mOne = True
                if tomato[z][y][x] == 1:
                    one = True
    return (mOne, zero, one)

for z in range(H):
    for y in range(N):
        tomato[z][y] = list(map(int, sys.stdin.readline().split()))
        for x in range(M):
            visited[(z, y, x)] = False
            if tomato[z][y][x] == 1 : 
                goto.append((z, y, x))

goto.append((-1, -1, -1))

if not check()[1]: # 0이 하나도 없는 경우
    print(0)
    exit()
if not(check()[0] or check()[2]): # 모두 0인 경우
    print(-1)
    exit()
    
k = 0
while goto:
    g = goto.pop(0)

    if g == (-1, -1, -1) and goto: 
        k += 1
        goto.append((-1, -1, -1))
        continue
    if not goto: break

    if visited[(g[0], g[1], g[2])] == False:
        visited[(g[0], g[1], g[2])] = True
        tomato[g[0]][g[1]][g[2]] = 1
        if g[0] - 1 >= 0 and tomato[g[0] - 1][g[1]][g[2]] == 0: goto.append((g[0] - 1, g[1], g[2]))
        if g[0] + 1 < H and tomato[g[0] + 1][g[1]][g[2]] == 0: goto.append((g[0] + 1, g[1], g[2]))
        if g[1] - 1 >= 0 and tomato[g[0]][g[1] - 1][g[2]] == 0: goto.append((g[0], g[1] - 1, g[2]))
        if g[1] + 1 < N and tomato[g[0]][g[1] + 1][g[2]] == 0: goto.append((g[0], g[1] + 1, g[2]))
        if g[2] - 1 >= 0 and tomato[g[0]][g[1]][g[2] - 1] == 0: goto.append((g[0], g[1], g[2] - 1))
        if g[2] + 1 < M and tomato[g[0]][g[1]][g[2] + 1] == 0: goto.append((g[0], g[1], g[2] + 1))


if not check()[1]: print(k)
else: print(-1)

# 반례
# 10 1 1
# 1 0 0 0 0 0 0 0 0 1