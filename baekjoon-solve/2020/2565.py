import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
arr.sort()

seq = [1] * N

for i in range(1, N):
    maxSeq = 0
    for j in range(i):
        if arr[j][1] < arr[i][1] and seq[j] > maxSeq:
            maxSeq = seq[j]
    seq[i] += maxSeq

print(N - max(seq))