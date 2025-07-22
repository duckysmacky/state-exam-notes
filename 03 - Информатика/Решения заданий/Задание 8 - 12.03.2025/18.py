from itertools import product, permutations

cnt = 0
sogl, glas = 'DCB', 'AE'
for word in product(glas + sogl, repeat=4):
    g = [x for x in word if x in glas]
    s = [x for x in word if x in sogl]
    if g == sorted(g) and s == sorted(s, reverse=True):
        i_g = len(g)
        i_s = 4 - len(s)
        if all(x in glas for x in word[:i_g]) and all(x in sogl for x in word[i_s:]):
            print(word)
            cnt += 1
print(cnt)
