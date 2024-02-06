arr = [list(map(int, input().split())) for _ in range(9)]
zeroIdx = []

for i in range(81) :
    if arr[i // 9][i % 9] == 0 : zeroIdx.append(i)

def f(times) :
    if times == len(zeroIdx) :
        for i in range(9) :
            print(" ".join(map(str, arr[i])))
        exit()    
    
    row = zeroIdx[times] // 9
    col = zeroIdx[times] % 9
    
    availNum = [1]*10
    for i in range(9) :
        availNum[arr[row][i]] = 0
        availNum[arr[i][col]] = 0
    for i in arr[(row // 3) * 3 : ((row + 3) // 3) * 3] :
        for j in i[(col // 3) * 3 : ((col + 3) // 3) * 3] : 
            availNum[j] = 0
    
    for i in range(1, 10) :
        if availNum[i] == 1 :
            arr[row][col] = i
            f(times + 1)
            arr[row][col] = 0

f(0)    

