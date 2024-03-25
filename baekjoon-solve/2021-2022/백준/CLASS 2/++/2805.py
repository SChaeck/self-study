n, m = map(int, input().split())
li = list(map(int, input().split()))

def bin(low, high) :
    mid = (low + high) // 2
    t = 0
    for i in li : 
        if i - mid > 0 :
            t += i - mid
    if t >= m :
        if abs(high - low) <= 1 :
            j = 0
            for i in li : 
                if i - high > 0 :
                    j += i - high    
            if j >= m :
                return high
            else : return low
        return bin(mid, high)
    else :
        return bin(low, mid)

print(bin(0, max(li)))