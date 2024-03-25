n1, n2 = map(int, input().split())

if n1 == n2 :
    print(n1)
    print(n1)

else :
    if n1 < n2 : # 계산하기 쉽게 n1 >= n2로 변경
        n1, n2 = n2, n1

    for i in range(n1//2 if n1//2 < n2 else n2, 0, -1) :
        if n1 % i == 0 and n2 % i == 0 :
            # 최대공약수
            GCF = i
            break
        
    print(GCF)
    print(n1 * (n2 // GCF))