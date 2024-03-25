n, m = map(int, input().split())
seq = []

def func(lat) :
    if len(seq) == m :
        print(' '.join(map(str, seq)))
        return
    
    for i in range(lat, n + 1) :
        seq.append(i)
        func(i)
        del seq[-1]
        
func(1)

# def func() :
#     if len(seq) == m :
#         print(' '.join(map(str, seq)))
#         return
    
#     for i in range(1, n+1) :
#         if len(seq) == 0 or i >= seq[-1] :
#             seq.append(i)
#             func()
#             del seq[-1]
            
# func()
