N = int(input())
cnt = 0
for i in range(N) :
    word = list(input())
    word_copy = word.copy()
    word_set = set(word)
    for i in range(len(word)-1) :
        if word[i] == word[i+1] :
            word_copy.remove(word[i])
    if len(word_set) == len(word_copy) :
        cnt += 1

print(cnt)