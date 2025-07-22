from fnmatch import fnmatch

mask = "3261??64*"
for num in range(1000000, 10 ** 9 - 1):
    if num % 163 == 0 and fnmatch(str(num), mask):
        print(num, num // 163)