from itertools import product

letters = "ПЕРПЕНДИКУЛЯР"
pattern = "ПЛАНДИР"
sogl = "ПРНДКЛР"
glas = "ЕИУЯ"

extra_r = 14 - len(pattern)
cnt = 0
for extra in product(set(letters), repeat=extra_r):
    for i in range(len(extra)):
        left, right = extra[:i], extra[i:]
        word = ''.join(left) + pattern + ''.join(right)
        if pattern in word and word[0] not in sogl and word[1] not in sogl and word[-1] not in sogl and word[-2] not in sogl:
            print(word)
            cnt += 1
print(cnt)
