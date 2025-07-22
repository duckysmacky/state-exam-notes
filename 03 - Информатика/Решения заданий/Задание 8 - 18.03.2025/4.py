from itertools import product, permutations

def base(x, p):
    num = ''
    while x > 0:
        num += str(x % p)
        x //= p
    return num[::-1]

for i, w in enumerate(product("ВИКОРТЯ", repeat=6), 0):
    word = ''.join(w)
    if word[0] == 'Т' and word.count('О') == 3:
        print(base(i, 7))
