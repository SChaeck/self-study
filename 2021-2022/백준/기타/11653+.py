N = int(input())

while(N != 1) :
    k = 2 # N을 분해할 변수

    while 1 :
        if N % k == 0 :
            print(k)
            N = N // k
            break
        
        elif k > N ** 0.5 :
            print(N)
            N = 1
            break
        
        k += 1
