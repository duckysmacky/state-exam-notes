from fnmatch import fnmatch

for n in range(123042593, 10 ** 12, 4013):
    num = str(n)
    if fnmatch(num, "123?4*5679"):
        if n % 4013 == 0:
            print(n, n // 4013)
