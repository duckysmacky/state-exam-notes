from itertools import product

cnt = 0
for num in product("01234567", repeat=5):
    if num[0] not in "0246" and num[-1] not in "15" and num.count('7') <= 1:
        cnt += 1
print(cnt)