from fnmatch import fnmatch

for num in range(0, 10 ** 8, 98):
    if fnmatch(str(num), "12*678?"):
        print(num, num // 98)