import sys

s = set()
cnt = 0

N = int(sys.stdin.readline())
for _ in range(N) :
    str = sys.stdin.readline().rstrip()
    if str == "ENTER" :
        cnt += len(s)
        s.clear()
        continue
    s.add(str)
else : cnt += len(s)

print(cnt)