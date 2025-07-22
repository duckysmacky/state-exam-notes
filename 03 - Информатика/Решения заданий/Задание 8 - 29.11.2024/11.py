from itertools import product

cnt = 0
for num in product("01234", repeat=4):
    if num[0] != '0' and num[0] > num[1] > num[2] > num[3]:
        cnt += 1
print(cnt)