N, X = map(int, input().split())
list1 = list(map(int, input().split()))

print(*filter(lambda a : a < X, list1))