import sys

N = int(sys.stdin.readline()) # sys.stdin.readline()
st = set()
for i in range(N) :
    st.add(sys.stdin.readline().rstrip()) # sys.stdin.readline().rstrip()
li = sorted(st)
li.sort(key = len)

print(*li, sep = "\n")