import sys
sys.setrecursionlimit(10**6)
T = int(input())

def cut(x, y) :
    li[x][y] = 0   
    if x != w-1 and li[x+1][y] : cut(x+1,y)
    if x != 0 and li[x-1][y] : cut(x-1,y)
    if y != h-1 and li[x][y+1] : cut(x,y+1)
    if y != 0 and li[x][y-1] : cut(x,y-1)

for _ in range(T) :
    w, h, l = map(int, input().split())
    cnt = 0
    li = [[0 for _ in range(h)] for _ in range(w)]

    for _ in range(l) :
        a, b = map(int, input().split())
        li[a][b] = 1

    for i in range(w) :
        for j in range(h) :
            if li[i][j] :
                cnt += 1
                cut(i, j)

    print(cnt)