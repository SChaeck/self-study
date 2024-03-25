T = int(input())

for i in range(T) :
    li = list(map(int, input().split()))
    leg = ((li[3]-li[0])**2 + (li[4]-li[1])**2)**0.5

    if leg > li[2] + li[5] : # 안 맞을 때
        print(0)
    elif leg == li[2] + li[5] : # 딱 맞을 때
        print(1)
    elif leg < li[2] + li[5] : 
        if leg == 0 : # 원의 중심이 같을 때
            if li[2] == li[5] :
                print(-1) # 반지름이 같을 때
            else :
                print(0) # 반지름이 다를때
        elif abs(li[5] - li[2]) > leg :          
            print(0) # 원이 다른 원 안에 있어서 좌표가 0개
        elif abs(li[5] - li[2]) == leg :
            print(1) # 원이 다른 원 안에 있는데 하나가 닿을 때
        else :
            print(2) # 원과 다른 원이 2점에서 만날 때
        
