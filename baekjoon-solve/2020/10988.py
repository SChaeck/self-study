str = input()

for i in range(int(len(str)/2)) :
    if(str[i] != str[-(i+1)]) :
        print(0)
        exit()
print(1)