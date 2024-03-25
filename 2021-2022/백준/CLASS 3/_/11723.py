import sys

T = int(sys.stdin.readline())
s = set()

for _ in range(T) :
    com = sys.stdin.readline().split()
    if com[0] == 'add' :
        s.add(int(com[1]))
    elif com[0] == 'remove' :
        if int(com[1]) in s :
            s.remove(int(com[1]))
    elif com[0] == 'check' :
        if int(com[1]) in s :
            print(1)
        else : print(0)
    elif com[0] == 'toggle' :
        if int(com[1]) in s :
            s.remove(int(com[1]))
        else : s.add(int(com[1]))
    elif com[0] == 'all' :
        s = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif com[0] == 'empty' :
        s.clear()
