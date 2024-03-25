import sys

N = int(input())
conv_list = []
for _ in range(N):
    s = list(map(int, sys.stdin.readline().split()))
    conv_list.append(s)
conv_list.sort(key=lambda x: (x[1], x[0]))

count = 1
bef_conv = conv_list[0]
for conv in conv_list[1:]:
    if bef_conv[1] <= conv[0]:
        bef_conv = conv
        count += 1

print(count)