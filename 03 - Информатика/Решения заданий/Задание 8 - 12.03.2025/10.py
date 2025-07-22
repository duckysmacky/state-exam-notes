from itertools import product, permutations

cnt = 0
for word in set(permutations('ПРОЦЕССОР')):
    word = ''.join(word)
    if sum(x in word for x in ['ПРО', 'ЦЕС', 'СОР']) == 0:
        cnt += 1
print(cnt)
