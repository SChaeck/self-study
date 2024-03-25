n, m = list(map(int, input().split()))
arr = [[0 for c in range(m)] for r in range(n)]

for i in range(n) :
    arr[i][:m] = list(map(int, input().split()))

for i in range(n) :
    arr2 = list(map(int, input().split()))
    for j in range(m) :
        arr[i][j] += arr2[j]
    
for i in range(n) :
    for j in range(m) :
        print(arr[i][j], end = " ")
    print()