from collections import deque
MAX_TIME = 10 ** 5

N, K = map(int, input().split())

if K <= N: print(N-K)
else:
    bfs = [0]*(MAX_TIME+1)
    bfs[N] = 0
    goto = deque()
    goto.append(N)
    
    while goto:
        t = goto.popleft()
        if t == K:
            print(bfs[t])
            break
        for dt in (t-1, t+1, 2*t):
            if 0 <= dt <= MAX_TIME and not bfs[dt]:
                bfs[dt] = bfs[t]+1
                goto.append(dt)
