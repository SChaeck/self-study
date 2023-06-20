arr = [['0' for j in range(15)] for i in range(5)]

print(arr)
    
for i in range(5) :
    arr[i][:15] = input()

print(arr)

# for j in range(15) :
#     print(arr[:5][j])