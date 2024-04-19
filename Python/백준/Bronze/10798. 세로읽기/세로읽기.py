arr = [["" for j in range(15)] for i in range(5)]

for i in range(5) :
    str = input()
    for j in range(len(str)) :
        arr[i][j] = str[j]

for j in range(15) :
    for i in range(5) :
        print(arr[i][j], end = "")