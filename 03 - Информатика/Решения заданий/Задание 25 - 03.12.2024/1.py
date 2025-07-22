from fnmatch import fnmatch

for num in range(5943, 10 ** 10, 5943):
    if fnmatch(str(num), "73*?859?"):
        print(num, num // 5943)