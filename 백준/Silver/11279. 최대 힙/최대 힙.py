import sys
from heapq import heappush, heappop

N = int(input())

heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else: 
            print(-1 * heappop(heap))
    else:
        heappush(heap, -1 * x)