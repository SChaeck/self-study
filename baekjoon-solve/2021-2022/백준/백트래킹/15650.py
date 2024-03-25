N, M = map(int, input().split())
seq = []

def func() :
    if len(seq) == M :
        print(' '.join(map(str, seq)))
        return
    
    for i in range(1, N+1) :
        if len(seq) == 0 or seq[-1] < i :
            seq.append(i)
            func()
            del seq[-1]

func()