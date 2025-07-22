from itertools import product

cnt = 0
for num in product("0123456789", repeat=4):
    num = ''.join(num)
    if num[0] != '0' and len(set(num)) == len(num):
        for d in "02468":
            num = num.replace(d, 'a')
        for d in "13579":
            num = num.replace(d, 'b')
        if "aa" not in num and "bb" not in num:
            cnt += 1
print(cnt)