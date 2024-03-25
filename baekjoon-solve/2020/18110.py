import sys

def rnd(num) :
    if num % 1 >= 0.5 : return int(num) + 1
    else : return int(num) 

N = int(sys.stdin.readline())
excep = rnd(N*0.15)
point = []

for i in range(N) :
    point.append(int(sys.stdin.readline()))
point.sort()

su = sum(point[excep:N-excep])
if N == 2*excep : result = 0
else : result = rnd(su/(N-2*excep))

print(result)