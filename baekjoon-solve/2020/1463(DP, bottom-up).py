n = int(input())

times = [0] * (10**6 + 1)

for i in range(2, n+1):
    times[i] = times[i-1] + 1
    if i % 2 == 0: times[i] = min(times[i], times[i//2] + 1)
    if i % 3 == 0: times[i] = min(times[i], times[i//3] + 1)

print(times[n])