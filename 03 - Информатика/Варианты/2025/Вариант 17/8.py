from itertools import product

cnt = 0
for num in product("01234567", repeat=11):
    nechet = [int(x) % 2 != 0 for x in num]
    if sum(nechet) == 4 and '11' not in ''.join([str(int(x)) for x in nechet]):
        print(''.join([str(int(x)) for x in nechet]))
        print(''.join(num), int(''.join(num), 8))
        cnt += 1
print(cnt)
