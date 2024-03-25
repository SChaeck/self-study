import sys
k, n = map(int, sys.stdin.readline().split())
# 가지고 있는 랜선의 개수 k, 필요한 랜선의 개수 n
li = []

def binary_search(low, high) :
    mid = (low + high) // 2
    t = 0
    for i in li :
        t += i // mid
    if t >= n :
        if abs(high - low) <= 1:
            j = 0
            for i in li :
                j += i // high
            if j >= n :
                return high
            else : return low
        return binary_search(mid, high)
    else :
        return binary_search(low, mid)
 
    
for _ in range(k) :
    li.append(int(sys.stdin.readline()))

print(binary_search(1, max(li)))