import re

file = open("1.txt")
text = file.readline()

matches = re.findall(r"[1-9AB][0-9AB]*[0369]", text)
print(len(max(matches, key=len)))