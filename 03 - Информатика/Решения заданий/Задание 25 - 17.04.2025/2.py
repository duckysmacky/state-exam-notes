from fnmatch import fnmatch

div = 76
for num in range(div, 10 ** 8, div):
    if fnmatch(str(num), "34*?55?") and num % div == 0 and str(num).count('3') == 2:
        print(num, num // div)