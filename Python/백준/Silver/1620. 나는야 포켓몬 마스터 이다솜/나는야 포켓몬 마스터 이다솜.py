import sys

n, m = map(int, sys.stdin.readline().split())

dic = {}

for i in range(n) :
    name = sys.stdin.readline().rstrip()
    dic[str(i+1)] = name

re_dic = dict(map(reversed, dic.items()))

for i in range(m) :
    order = sys.stdin.readline().rstrip()
    if order in dic :
        print(dic[order])
    else : 
        print(re_dic[order])