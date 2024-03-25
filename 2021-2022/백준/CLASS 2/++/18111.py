# 블록 중에 가장 높은 위치와 낮은 위치 사이에 답이 존재 해야 함.
# 최소시간으로 코드 짜는게 맞고 최소시간이 여러개면 그중에 가장
# 높은 값을 출력하는 코드임 아 내일 다시 ㄱ
# 이진검색으로는 기준이 너무 애매해서 완전탐색으로 변경
import sys

n, m, b = map(int, sys.stdin.readline().split())
inv = [[] for i in range(n)]
tm_dic = {} # dictionary
mx = -1
mn = 257

for i in range(n) :
    inv[i] = list(map(int, sys.stdin.readline().split()))
    if max(inv[i]) > mx :
        mx = max(inv[i])
    if min(inv[i]) < mn :
        mn = min(inv[i])


for h in range(mn, mx+1) :
    time = 0
    b1 = 0  
    for i in range(n) :
        for j in range(m) :
            k = inv[i][j] - h
            if k > 0 :
                time += 2*k
                b1 += k
            elif k < 0 :
                time += -k
                b1 -= -k
    if b1 + b >= 0 :
        tm_dic[time] = h                   

print(min(tm_dic), tm_dic[min(tm_dic)])

# 높이가 아니라 블록 개수를 출력했고,
# 두개 다 확인하지 않음