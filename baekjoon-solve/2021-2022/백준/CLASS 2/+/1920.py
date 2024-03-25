n = int(input())
n_li = list(map(int, input().split()))
m = int(input())
m_li = list(map(int, input().split()))

n_li.sort()
loc = 0

def binary_search(low, high, target) :
    global loc
    mid = (low + high) // 2
    if low >= high :
        if n_li[low] == target :
            return True
        else : return False
    if n_li[mid] == target :
        loc = mid
        return True
    elif n_li[mid] < target :
        return binary_search(mid+1, high, target)
    elif n_li[mid] > target :
        return binary_search(low, mid-1, target)



for i in m_li :
    a = binary_search(0, n - 1, i) 
    if a :
        print(1)
    else :
        print(0)     