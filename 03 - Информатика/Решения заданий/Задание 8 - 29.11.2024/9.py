from itertools import product

cnt = 0
for num in product("0123456", repeat=6):
    num = ''.join(num)
    if num[0] != '0' and num.count('5') == 2 and all(f"{n}5" not in num and f"5{n}" not in num for n in "0246"):
        cnt += 1
print(cnt)