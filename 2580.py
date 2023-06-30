arr = [list(map(int, input().split())) for _ in range(9)]

def f(idx) :
    
    row = idx // 9
    col = idx % 9
    
    availNum = [1]*10 # 0~9까지 표현하는데 0은 걍 무시
    for i in arr[row][:] :
        availNum[i] = 0
    for i in arr[:][col] :
        availNum[i] = 0
    for i in arr[((row) // 3) * 3 : ((row) + 3 // 3) * 3][((col) // 3) * 3 : ((col) + 3 // 3) * 3] :
        availNum[i] = 0
    
    for i in range(1, 10) :
        if availNum[i] == 1 :
            arr[row][col] = i
            f(i)
            arr[row][col] = 0

# 가로, 세로, 3x3칸에서 들어갈 수 있는 숫자를 추려서 
# 넣고 재귀문 반복하면 될 것 같은데


for i in range(81) :
    if arr[i // 9][i % 9] == 0 : f(i) # 0을 찾고 
    
    ##### 0 위치를 찾고 그 위치를 저장하는 배열이 필요할듯
    

