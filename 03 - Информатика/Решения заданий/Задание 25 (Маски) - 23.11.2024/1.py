from fnmatch import fnmatch

ans = ""
for num in range(0, 10 ** 5, 134):
    if fnmatch(str(num), "1?7*"):
       ans += str(bin(num)[2:].count('1'))
print(ans)