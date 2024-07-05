def break_down(i) :
    j = i
    a = str(i)
    for t in range(len(a)) :
        j += int(a[t])

    return j

k = int(input())

for i in range(k) :
    if break_down(i) == k :
        print(i)
        break
else : print(0)