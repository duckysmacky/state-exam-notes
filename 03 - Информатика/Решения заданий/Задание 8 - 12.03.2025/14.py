from itertools import product, permutations

cnt = 0
for num in product('01234567', repeat=5):
    num = ''.join(num)
    if num[0] == '0': continue
    if num[0] not in '13579' and num[-1] not in '34' and num.count('5') <= 1:
        cnt += 1
print(cnt)
