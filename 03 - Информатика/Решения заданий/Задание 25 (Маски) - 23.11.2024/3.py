from fnmatch import fnmatch

for num in range(0, 10 ** 8, 31):
    if fnmatch(str(num), "123*578"):
        print(num, num // 31)