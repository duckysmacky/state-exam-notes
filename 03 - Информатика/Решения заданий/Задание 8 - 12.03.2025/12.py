from itertools import product, permutations

cnt = 0
for word in product(set('ЗАРЯ'), repeat=5):
    word = ''.join(word)
    if word.count('Р') <= 1 and word[0] != 'Р' and word[-1] != 'Р' and 'РЯ' not in word and 'ЯР' not in word:
        cnt += 1
print(cnt)
