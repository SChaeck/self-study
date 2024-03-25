input()
st = input()
asc_st = list(map(ord, st))
t = 0
for i in range(len(st)) :
    t += (asc_st[i] - 96) * (31**i)

print(t % 1234567891)