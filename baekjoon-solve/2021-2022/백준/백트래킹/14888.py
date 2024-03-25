n = int(input())
li = list(map(int, input().split()))
p, m, M, d = map(int, input().split())
oper = [0] * p + [1] * m + [2] * M + [3] * d
max = -1000000000
min = 1000000000
ans = li[0]
i_li = []

def func(k) :
    global max, min, ans
    if k == n :
        if ans > max :
            max = ans
        if ans < min :
            min = ans
    else :
        for i in range(len(oper)) :
            if not i in i_li :
                dummy = ans
                if oper[i] == 0 :
                    ans = ans + li[k]
                elif oper[i] == 1 :
                    ans = ans - li[k]
                elif oper[i] == 2 :
                    ans = ans * li[k]
                elif oper[i] == 3 :
                    ans = ans // li[k]
                i_li.append(i)
                
                func(k+1)
                ans = dummy
                del i_li[-1]

func(1)
print(max)
print(min)
