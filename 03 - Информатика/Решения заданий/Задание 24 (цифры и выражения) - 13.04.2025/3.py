import re

file = open("3.txt")
text = file.readline()

num = r"(?:0|[1-9]\d*)"
pattern = fr"{num}(?:[+*]{num})*"
matches = re.findall(pattern, text)
best = max(matches, key=len)
print(best, len(best))