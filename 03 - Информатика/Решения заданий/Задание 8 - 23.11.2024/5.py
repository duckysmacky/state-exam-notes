from itertools import permutations

cnt = 0
for word in permutations("ТАВРИЯ",  r=5):
    if word[0] != 'В' and "ИЯ" not in ''.join(word):
        cnt += 1
print(cnt)