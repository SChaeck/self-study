N = int(input())

i = 2
while(N != 1) :
    if i > N ** 0.5 :
        break
    if N % i == 0 :
        N = N // i
        print(i)
        break
