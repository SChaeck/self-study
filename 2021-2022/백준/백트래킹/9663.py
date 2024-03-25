n = int(input())
board = [0] * n
cnt = 0

def is_promising(k) :
    for j in range(k) :
        if board[j] == board[k] or abs(k - j) == abs(board[k]-board[j]) :
            return False
        
    return True

def func(k) :
    global cnt
    if k == n :
       cnt += 1
       
    else :
        for i in range(n) :
            board[k] = i
            if is_promising(k) :
                func(k+1)

func(0) 

print(cnt)