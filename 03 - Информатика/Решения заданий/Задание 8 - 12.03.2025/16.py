from itertools import product, permutations
from string import digits, ascii_uppercase

alph = digits + ascii_uppercase
cnt = 0
for num in product(alph[:21], repeat=6):
    if num[0] == '0': continue
    if num.count('6') == 1 and sum(int(x, 21) > 11 for x in num) >= 3:
        cnt += 1
print(cnt)
