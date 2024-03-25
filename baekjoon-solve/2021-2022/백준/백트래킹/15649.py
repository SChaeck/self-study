n, m = map(int, input().split())
seq = []

def func() :
    if len(seq) == m : # 조건문
        print(' '.join(map(str, seq)))
        return
    
    for i in range(1, n+1) : # 수열에 수를 추가
        if not i in seq :
            seq.append(i)
            func()
            del seq[-1]

func()