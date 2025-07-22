import re

file = open("2.txt")
text = file.readline()

num = r"[1-9]\d*"
pattern = fr"{num}(?:[+*]{num})*"
matches = re.findall(pattern, text)
best = max(matches, key=len)
print(best, len(best))