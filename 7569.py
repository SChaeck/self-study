M, N, H = map(int, input().split())

tomato = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
goto = []

def check():
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if tomato[z][y][x] == 0:
                    return False
    return True

for z in range(H):
    for y in range(N):
        tomato[z][y] = list(map(int, input().split()))
        for x in range(M):
            if tomato[z][y][x] == 1 : 
                goto.append((z, y, x))
                tomato[z][y][x] = 0

goto.append((-1, -1, -1))

k = 0

while goto:
    g = goto.pop(0)

    if g == (-1, -1, -1): 
        k += 1
        goto.append((-1, -1, -1))
        continue

    if tomato[g[0]][g[1]][g[2]] == 0:
        tomato[g[0]][g[1]][g[2]] = 1
        if g[0] - 1 >= 0 and tomato[g[0] - 1][g[1]][g[2]] == 0: goto.append((g[0] - 1, g[1], g[2]))
        if g[0] + 1 < H and not tomato[g[0] + 1][g[1]][g[2]] == 0: goto.append((g[0] + 1, g[1], g[2]))
        if g[1] - 1 >= 0 and not tomato[g[0]][g[1] - 1][g[2]] == 0: goto.append((g[0], g[1] - 1, g[2]))
        if g[1] + 1 < N and not tomato[g[0]][g[1] + 1][g[2]] == 0: goto.append((g[0], g[1] + 1, g[2]))
        if g[2] - 1 >= 0 and not tomato[g[0]][g[1]][g[2] - 1] == 0: goto.append((g[0], g[1], g[2] - 1))
        if g[2] + 1 < M and not tomato[g[0]][g[1]][g[2] + 1] == 0: goto.append((g[0], g[1], g[2] + 1))


if check(): print(k)
else: print(-1)
