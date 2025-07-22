from itertools import permutations

cnt = 0
for word in permutations("БАВЛЫ", r=4):
    if word[0] != 'В' and "АЫ" not in ''.join(word):
        cnt += 1
print(cnt)