li = list(map(int, input().split()))
li.sort()
se_li = set(li)

if len(se_li) == 1 :
    print(10000 + li[0]*1000)
elif len(se_li) == 2 :
    print(1000 + li[1]*100)
else :
    print(li[2]*100)
    
