import sys
input = sys.stdin.readline

def chess_check(arr) :
    arr = list(arr)    
    cnt_W = 0
    cnt_B = 0
    for i in range(8) :
        for j in range(8) :
            if not((i + j) % 2) :
                if arr[i][j] != 'W' : cnt_W += 1
                else : cnt_B += 1
            else :
                if arr[i][j] != 'B' : cnt_W += 1
                else : cnt_B += 1
    
    return cnt_W if cnt_W < cnt_B else cnt_B

N, M = map(int, input().split())
arr = [None] * N
s_min = 64
for i in range(N) :
    arr[i] = list(input().rstrip()) # .rstrip()

for i in range(N - 8, -1, -1) :
    for j in range(M - 8, -1, -1) :
        t = chess_check(row[j:j+8] for row in arr[i:i+8])
        if s_min > t :
            s_min = t     

print(s_min)