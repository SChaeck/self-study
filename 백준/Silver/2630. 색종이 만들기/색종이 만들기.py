import sys

def twoD_list_sum(l, res = 0):
    for i in l:
        res += sum(i)
    return res

def square_check(p):
    global w_cnt, b_cnt
    p_len = len(p)
    list_sum = twoD_list_sum(p)

    if list_sum == p_len*p_len or list_sum == 0: # 네 칸이 모두 같은 값인 경우
        if p[0][0] == 0: w_cnt += 1
        else: b_cnt += 1
        return
    
    p1 = []
    p2 = []
    p3 = []
    p4 = []

    for i, l in enumerate(p):
        if i < p_len / 2:
            p1.append(l[:p_len//2])
            p2.append(l[p_len//2:])
        else:
            p3.append(l[:p_len//2])
            p4.append(l[p_len//2:])

    square_check(p1)
    square_check(p2)
    square_check(p3)
    square_check(p4)
    

N = int(sys.stdin.readline())
paper = []
for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

w_cnt = b_cnt = 0
square_check(paper)

print(w_cnt)
print(b_cnt)