def hansu(n) :
    cnt = 0
    if n >= 100 :
        cnt = 99
        for i in range(100, n + 1) :
            if (i//100 - i%100//10) == (i%100//10 - i%10) :
                cnt += 1
    else :
        cnt = n
    return cnt

num = int(input())
print(hansu(num))