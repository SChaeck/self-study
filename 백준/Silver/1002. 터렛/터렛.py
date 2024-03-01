T = int(input())

for i in range(T) :
    li = list(map(int, input().split()))
    leg = ((li[3]-li[0])**2 + (li[4]-li[1])**2)**0.5

    if leg > li[2] + li[5] :
        print(0)
    elif leg == li[2] + li[5] :
        print(1)
    elif leg < li[2] + li[5] :
        if leg == 0 :
            if li[2] == li[5] :
                print(-1)
            else :
                print(0)
        elif abs(li[5] - li[2]) > leg :
            print(0)
        elif abs(li[5] - li[2]) == leg :
            print(1)
        # 원이 다른 원 안에 있어서 0개일 때와 
        # 원이 다른 원 안에 있는데 하나가 닿을 때
        else :
            print(2)
        
