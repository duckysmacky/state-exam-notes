import re

file = open("3.txt")

cnt = 0
pattern = r"^\d+(?:[+\-*]\d+)*$"
for line in file:
    if re.match(pattern, line):
        cnt += 1
print(cnt)
