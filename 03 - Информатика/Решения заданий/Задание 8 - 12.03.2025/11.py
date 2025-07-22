from itertools import product, permutations

cnt = 0
for word in product(set('КАБАЧОК'), repeat=4):
    w = ''.join(word)
    sogl = 'КБЧ'
    for l in sogl:
        w = w.replace(l, '*')
    if word[0] in 'КБЧ' and word[-1] in 'АО' and '**' not in w:
        cnt += 1
print(cnt)
