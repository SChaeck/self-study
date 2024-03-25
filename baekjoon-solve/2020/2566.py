arr = []
for i in range(9) :
    arr += list(map(int, input().split()))

max = int(max(arr))
print(max)
print(int(arr.index(max) / 9) + 1, arr.index(max) % 9 + 1)