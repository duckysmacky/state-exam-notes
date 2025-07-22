from fnmatch import fnmatch

for num in range(2049, 10 ** 9 + 1, 2049):
    if fnmatch(str(num), "32*21?4") and num % 2049 == 0:
        print(num, num // 2049)
