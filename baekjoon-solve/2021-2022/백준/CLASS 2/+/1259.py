while True :
    n = input()
    if n == '0' : break
    rn = n[::-1]
    if rn == n :
        print('yes')
    else :
        print('no')