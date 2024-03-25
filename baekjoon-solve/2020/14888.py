_ = input()
num = list(map(int, input().split()))
oper = list(map(int, input().split()))
maxResult = -10**9
minResult = 10**9

def f(result, numIdx) :
    global maxResult, minResult
    if not any(oper) :
        maxResult = max(maxResult, result)
        minResult = min(minResult, result)
        return

    for i in range(4) :
        if oper[i] != 0 :
            oper[i] -= 1
            if i == 0 : f(result + num[numIdx + 1], numIdx + 1)
            elif i == 1 : f(result - num[numIdx + 1], numIdx + 1)
            elif i == 2 : f(result * num[numIdx + 1], numIdx + 1)
            elif i == 3 : f(int(result / num[numIdx + 1]), numIdx + 1)
            oper[i] += 1

f(num[0], 0)
print(maxResult, minResult, sep = "\n")