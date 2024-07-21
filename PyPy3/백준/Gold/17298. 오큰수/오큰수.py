import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
stack = []
result = [-1] * N

stack.append(0)
for i in range(1, N) :
    while stack and a[stack[-1]] < a[i] :
        result[stack.pop()] = a[i]
    stack.append(i)

print(*result)