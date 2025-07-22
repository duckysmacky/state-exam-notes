from itertools import product, permutations

cnt = 0
for num in product('01234567', repeat=6):
    if num[0] == '0': continue
    num = ''.join(['a' if int(x) % 2 == 0 else 'b' for x in num])
    if 'aa' not in num and 'bb' not in num:
        cnt += 1
print(cnt)
