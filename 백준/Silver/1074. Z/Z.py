N, r, c = map(int, input().split())
sum = 0

def f(n, row, col) :
    global sum
    if n == 0 :
        print(sum)
        exit()
    
    if row < 2**(n-1) :
        if col < 2**(n-1) : # 1사분면
            f(n-1, row, col)
        else : # 2사분면
            sum += 2**(2*(n-1))
            f(n-1, row, col - 2**(n-1))
    else :
        if col < 2**(n-1) : # 3사분면
            sum += 2 * 2**(2*(n-1))
            f(n-1, row - 2**(n-1), col)
        else : # 4사분면
            sum += 3 * 2**(2*(n-1))
            f(n-1, row - 2**(n-1), col - 2**(n-1))

f(N, r, c)