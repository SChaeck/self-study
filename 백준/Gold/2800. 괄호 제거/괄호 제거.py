s = input()
stack = []
bracket_pair = []
print_set = set()

def RecursiveRemoveBracket(n):
    global s, bracket_pair, print_list
    if n == len(bracket_pair):
        return
    RecursiveRemoveBracket(n+1)
    s = s[ : bracket_pair[n][0]] + '_' + s[bracket_pair[n][0] + 1 : ]
    s = s[ : bracket_pair[n][1]] + '_' + s[bracket_pair[n][1] + 1 : ]
    print_set.add(s.replace('_', ''))
    RecursiveRemoveBracket(n+1)
    s = s[ : bracket_pair[n][0]] + '(' + s[bracket_pair[n][0] + 1 : ]
    s = s[ : bracket_pair[n][1]] + ')' + s[bracket_pair[n][1] + 1 : ]

for i, c in enumerate(s):
    if c == '(':
        stack.append(i)
    elif c == ')':
        left_index = stack.pop()
        bracket_pair.append((left_index, i))

RecursiveRemoveBracket(0)

print_list = list(print_set)
print_list.sort()

for p in print_list:
    print(p)