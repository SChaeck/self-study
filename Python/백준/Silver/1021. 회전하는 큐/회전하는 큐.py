from collections import deque

size, many = map(int, input().split())
d = deque([0]*size)
ext = list(map(int, input().split()))
cnt = 0

for i in range(many) : 
    d[ext[i] - 1] = i + 1 

for i in range(1, many + 1) :
    ind = d.index(i)
    if ind <= len(d) // 2 :
        while d[0] != i :
            d.append(d.popleft())
            ind -= 1
            cnt += 1
    else : 
        while d[0] != i :
            d.appendleft(d.pop())
            ind += 1
            cnt += 1
    d.popleft()
print(cnt)