import sys

N, M = map(int, sys.stdin.readline().split())
d = {}

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) < M: continue
    elif word in d : d[word] += 1
    else : d[word] = 1

d = sorted(d.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))

for i in d :
    print(i[0])