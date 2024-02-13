T = int(input())

cnt0 = cnt1 = 0

def fibo(n) :
    global cnt0, cnt1
    
    
    if n == 0 :
        cnt0 += 1
        return 0
    elif n == 1 :
        cnt1 += 1
        return 1
    else :
        return fibo(n-1) + fibo(n-2)

for i in range(T) :
    n = int(input())
    
    fibo(n)
    print(cnt0, cnt1)
    cnt0 = cnt1 = 0