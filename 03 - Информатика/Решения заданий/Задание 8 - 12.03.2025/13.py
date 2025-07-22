from itertools import product, permutations

cnt = 0
for num in product('0123456', repeat=4):
    num = ''.join(num)
    a = ''.join(['*' if int(x) % 2 != 0 else x for x in num])
    if num[0] == '0': continue
    if num.count('5') == 1 and '2*' not in a and '*2' not in a:
        print(num, a)
        cnt += 1
print(cnt)
