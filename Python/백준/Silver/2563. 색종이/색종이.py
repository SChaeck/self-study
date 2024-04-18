import sys

arr = [[0 for i in range(100)] for j in range(100)]

d = int(input())
for k in range(d) :
    x, y = list(map(int, input().split()))
    for i in range(10) :
        for j in range(10) :
            arr[x+i][y+j] = 1
num = 0
for i in range(100) :
    num += arr[i].count(1)
print(num)