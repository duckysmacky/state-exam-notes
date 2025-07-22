import re

file = open("24var02.txt")
text = file.readline()

num = r"(?:[1-9]\d*|0)"
pattern = rf"{num}(?:[+-]{num})*"
matches = list(map(''.join, re.findall(pattern, text)))

print(len(max(matches, key=len)))
