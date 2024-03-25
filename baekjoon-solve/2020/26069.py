import sys

N = int(sys.stdin.readline())

s = {"ChongChong"}

for _ in range(N) :
    name1, name2 = sys.stdin.readline().rstrip().split()
    if name1 in s :
        s.add(name2)
    elif name2 in s :
        s.add(name1)

print(len(s))