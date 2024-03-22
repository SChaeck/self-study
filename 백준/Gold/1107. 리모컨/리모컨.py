target = int(input())
N = input()
if not N == '0' : broken = input().split()
else : broken = []

semi = 0
minR = abs(target - 100) 

if len(broken) == 10 : 
    print(minR)
    exit()

k = 0
while 1 : 
    flag1 = flag2 = True
    for i in range(len(broken)) : 
        if target - k < 0 : flag1 = False
        if flag1 and broken[i] in str(target - k) : flag1 = False
        if flag2 and broken[i] in str(target + k) : flag2 = False
        if not(flag1 or flag2) : break
    else : 
        if flag1 : 
            result = len(str(target - k)) + k
        elif flag2 : 
            result = len(str(target + k)) + k
        break
    k += 1

print(min(minR, result))