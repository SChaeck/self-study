N, M, V = map(int, input().split())
dfsArr = [V]
bfsArr = [V]

gph = [[False for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M) :
    i, j = map(int, input().split())
    gph[i][j] = True
    gph[j][i] = True

def dfs() :
    marked = [True] + [False] * N
    marked[V] = True
    goto = []
    for i in range(N, 0, -1) :
        if gph[V][i] and not marked[i] : # 간선이 있는 경우
            goto.append(i)
    
    while len(goto) != 0 :
        next = goto.pop()
        if not marked[next] :
            marked[next] = True
            dfsArr.append(next)
            for i in range(N, 0, -1) :
                if gph[next][i] and not marked[i]: # 간선이 있고 가지 않은 곳
                    goto.append(i)

def bfs() :
    marked = [True] + [False] * N
    marked[V] = True
    goto = []
    for i in range(1, N + 1) :
        if gph[V][i] and not marked[i] : # 간선이 있는 경우
            goto.append(i)
    
    while len(goto) != 0 :
        next = goto.pop(0)
        if not marked[next] :
            marked[next] = True
            bfsArr.append(next)
            for i in range(1, N + 1) :
                if gph[next][i] and not marked[i]: # 간선이 있고 가지 않은 곳
                    goto.append(i)

dfs()
bfs()

print(" ".join(map(str,dfsArr)))
print(" ".join(map(str,bfsArr)))