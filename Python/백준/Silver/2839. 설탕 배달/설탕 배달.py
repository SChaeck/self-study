kg = int(input())

for i in range(kg // 5, -1, -1) : 
    if (kg - 5*i) % 3 == 0 :
        print(int(i + (kg - 5*i) / 3))
        exit()
print(-1)