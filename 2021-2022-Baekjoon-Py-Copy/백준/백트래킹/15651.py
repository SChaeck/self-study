n, m = map(int, input().split())
seq = []

def func() :
    if len(seq) == m :
        print(' '.join(map(str, seq)))
        return
    
    for i in range(1, n + 1) :
        seq.append(i)
        func()
        del seq[-1]

func()