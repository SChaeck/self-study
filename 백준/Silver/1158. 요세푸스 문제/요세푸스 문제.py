from collections import deque

n, k = map(int, input().split())

yo = []
deq = deque([i for i in range(1, n+1)])
cnt = 0

while deq:
    cnt += 1
    num = deq.popleft()
    if cnt % k != 0: deq.append(num)
    else: yo.append(num)

print('<' + ', '.join(map(str, yo)) + '>')