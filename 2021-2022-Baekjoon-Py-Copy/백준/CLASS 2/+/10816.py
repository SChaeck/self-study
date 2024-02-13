from collections import Counter

input()
n_li = list(map(int, input().split()))
k = int(input())
m_li = list(map(int, input().split()))

cnt = Counter(n_li) 

for i in m_li :
    print(cnt[i], end = ' ')