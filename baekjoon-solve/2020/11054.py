import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
seq = [1] * n
revSeq = [1] * n
sumSeq = []

for i in range(1, n):
    maxSeq = 0
    for j in range(i):
        if num[j] < num[i] and seq[j] > maxSeq:
            maxSeq = seq[j]
    seq[i] += maxSeq

for i in range(n - 2, -1, -1):
    revMaxSeq = 0
    for j in range(i + 1, n):
        if num[j] < num[i] and revSeq[j] > revMaxSeq:
            revMaxSeq = revSeq[j]
    revSeq[i] += revMaxSeq

for i in range(n):
    sumSeq.append(seq[i] + revSeq[i])

print(max(sumSeq) - 1)