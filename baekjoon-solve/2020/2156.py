import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    num = int(sys.stdin.readline())
    arr.append([num, num, num])

if n == 1:
    print(num)
    exit()

arr[1][2] += arr[0][1]

if n > 2:
    arr[2][1] += arr[0][0]
    arr[2][2] += arr[1][1]
    for i in range(3, n): 
        arr[i][1] += max(max(arr[i - 3]), max(arr[i - 2]))
        arr[i][2] += arr[i - 1][1]

print(max(max(arr[n - 2]), max(arr[n - 1])))