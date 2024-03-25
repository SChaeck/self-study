board = [[0 for i in range(8)] for i in range(8)]

print('\n'.join(map(str,board)))
print()

# board[5][:] = 1

# for i in range(8) :
#     board[5][i] = 1

# board[5] = [1 for j in range(8)]

# for k in range(8) : # 세로 1
#     board[k][5] = 1
                    
for k in range(1, 8) : # 왼쪽 위 대각선 1
    if 3 + k > 7 or 2 + k > 7 :
        break
    board[3+k][2+k] = 1
                    
print('\n'.join(map(str,board)))

