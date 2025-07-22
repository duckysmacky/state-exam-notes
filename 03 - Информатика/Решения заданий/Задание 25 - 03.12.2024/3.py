from fnmatch import fnmatch

for num in range(123, int("FFFFFF", 16), 123):
    if fnmatch(hex(num)[2:], "F5*1?4"):
        print(hex(num)[2:], num // 123)