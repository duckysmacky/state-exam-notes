import re

file = open("2.txt")
text = file.readline()

matches = re.findall(r"\d+(?:[+\-*]\d+)+", text)
print(len(max(matches, key=len)))
