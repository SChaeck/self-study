n = int(input())
time_list = list(map(int, input().split()))
time_list.sort()
min_time = 0
min_sum = 0

for n in time_list:
    min_time += n
    min_sum += min_time

print(min_sum)