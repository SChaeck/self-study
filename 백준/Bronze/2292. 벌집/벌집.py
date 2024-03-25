N = int(input())

if N == 1 : 
    print(1)
    exit()

num = ((N - 5/4)/3)**(1/2) + 1.5
print(int(num))