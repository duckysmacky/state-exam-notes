from fnmatch import fnmatch

div = 5943
for num in range(div, 10 ** 10, div):
    if fnmatch(str(num), "73*?859?") and num % div == 0:
        print(num, num // div)