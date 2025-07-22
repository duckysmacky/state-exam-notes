from fnmatch import fnmatch

pattern = "1*34?5?9"
div = 31007
for num in range(div * 42, 10 ** 10 + 1, div):
    if fnmatch(str(num), pattern):
        if num % div == 0:
            print(num, num // div)
