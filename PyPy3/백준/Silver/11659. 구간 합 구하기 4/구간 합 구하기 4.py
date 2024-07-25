import sys

N, M = map(int, input().split())
numList = list(map(int, input().split()))
accumList = [numList[0]]*N

for i in range(1, N):
    accumList[i] = accumList[i-1] + numList[i]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(accumList[j-1] - accumList[i-2] if i-2 >= 0 else accumList[j-1])