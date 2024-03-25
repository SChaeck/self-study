n = int(input())
if n == 1:
    print(1)
else:
    dpTable = [0] * n
    dpTable[0] = 1
    dpTable[1] = 2
    for i in range(2, n):
        dpTable[i] = dpTable[i-1] + dpTable[i-2]
    print(dpTable[n-1] % 10007)