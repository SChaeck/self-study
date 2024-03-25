num = input()
save = int(num)
i = 0
while True :
    if len(num) == 1 :
        num = num + num
    else :
        num = num[1] + str((int(num[0])+int(num[1]))%10)
    i += 1
    if save == int(num) :
        break
print(i)