from fnmatch import fnmatch

for num in range(403, 10 ** 7, 403):
    if fnmatch(str(num), "12*?1*5"):
        print(num, num // 403)