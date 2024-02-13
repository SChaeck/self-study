def check_prime(num) :

    k = 2
    while 1 :
        if k > num ** 0.5 :
            return True
        elif not num % k :
            return False
        
        k += 1

T = int(input())

for i in range(T) :
    num = int(input())
    d = num//2
    while 1 :
        if check_prime(d) :
            if check_prime(num-d) :
                print(d, num-d)
                break
        d -= 1
