from itertools import product

def check(num: str) -> bool:
    return int(num[0]) % 2 == 0 and int(num[-1]) % 2 != 0
        
cnt = 0
for num in product("0123456", repeat=6):
    if num[0] != '0' and check(num) and num.count('5') <= 1:
        cnt += 1
print(cnt)