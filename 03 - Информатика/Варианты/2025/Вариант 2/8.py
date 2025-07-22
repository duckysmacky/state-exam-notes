from itertools import product
import re

def check(num: tuple) -> bool:
    num = ''.join(num)
    return not bool(re.search(r"([02468]0)|(0[02468])", num))

cnt = 0
for num in product("0123456", repeat=6):
    if num[0] != '0' and num.count('0') == 1 and check(num):
        print(num)
        cnt += 1
print(cnt)
