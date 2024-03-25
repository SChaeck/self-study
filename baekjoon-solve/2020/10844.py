N = int(input())

num = [[0 for _ in range(10)] for _ in range(N)]
num[N - 1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(N - 1, 0, -1):
    num[i - 1][1] += num[i][0] # 0인 경우
    num[i - 1][8] += num[i][9] # 9인 경우
    for j in range(1, 9):
        num[i - 1][j - 1] += num[i][j]
        num[i - 1][j + 1] += num[i][j]

print(sum(num[0]) % 1000000000)