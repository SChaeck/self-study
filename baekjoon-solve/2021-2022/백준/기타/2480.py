a, b, c = map(int, input().split())

price = 0

if a == b :
    if b == c :
        # 3개가 모두 같은 경우
        price = 10000 + a*1000
    else :
        # a와 b만 같은 경우
        price = 1000 + a*100
elif b == c :
    # b와 c만 같은 경우
    price = 1000 + b*100
elif a == c :
    # a와 c만 같은 경우
    price = 1000 + a*100
else :
    # 모두 다른 경우
    price = max(a, b, c)*100

print(price)
