import sys
input = sys.stdin.readline
t = int(input())
fibo_li = [-1] * 41
fibo_li[0] = 0, 1, 0
fibo_li[1] = 1, 0, 1

def fibo(n) :
    if fibo_li[n] != -1 :
        return fibo_li[n]
    else :
        fn1 = fibo(n-1)
        fn2 = fibo(n-2)
        fibo_li[n] = fn1[0]+fn2[0], fn1[1]+fn2[1], fn1[2]+fn2[2]
        return fibo_li[n]
    

for i in range(t) :
    n = int(input())
    a, z, o = fibo(n)
    print(z, o)