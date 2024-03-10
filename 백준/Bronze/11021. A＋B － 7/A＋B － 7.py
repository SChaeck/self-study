import sys

caseNum = int(input())

for i in range(0, caseNum) :
    num1, num2 = map(int, sys.stdin.readline().strip().split())
    print(f"Case #{i+1}: {num1+num2}")