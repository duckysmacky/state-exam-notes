from itertools import product

cnt = 0
for word in product("ОЛИВЬЕ_", repeat=6):
    word = ''.join(word)
    parts = list(filter(lambda x: len(x) > 0, word.split('_')))
    if len(parts) >= 3 and '__' not in word:
        print(word)
        cnt += 1
print(cnt)
