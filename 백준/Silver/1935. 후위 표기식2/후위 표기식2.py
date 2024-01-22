n = int(input())
postfix = input()
num_list = [int(input()) for _ in range(n)]

stack = []

for p in postfix:
    ac = ord(p)
    if 65 <= ac and ac <= 90:
        stack.append(num_list[ac-65])
    else:
        num2 = stack.pop()
        num1 = stack.pop()
        if p == '+': num = num1 + num2
        elif p == '-': num = num1 - num2
        elif p == '*': num = num1 * num2
        else: num = num1 / num2
        stack.append(num)

print('{:.2f}'.format(stack[0]))