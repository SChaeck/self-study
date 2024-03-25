import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
seq = [1] * n

for i in range(1, n):
    maxSeq = 0
    for j in range(i):
        if num[j] < num[i] and seq[j] > maxSeq:
            maxSeq = seq[j]
    seq[i] += maxSeq

print(max(seq))