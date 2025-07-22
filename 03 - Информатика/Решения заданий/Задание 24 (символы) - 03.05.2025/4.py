import re

file = open('4.txt')
text = file.readline()

nums = re.findall(r"[1-9AB][0-9AB]*", text)
good = list(filter(lambda x: int(x, 12) % 6 == 0, nums))
best = max(good, key=len)
print(best, len(best))