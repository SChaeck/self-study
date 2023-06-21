import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) < M: continue
    arr.append(word)

arr.sort()

arr = Counter(arr).most_common()

for i in arr :
    print(i[0])
