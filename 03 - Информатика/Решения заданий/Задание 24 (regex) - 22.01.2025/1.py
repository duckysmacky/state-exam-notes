import re

file = open("1.txt")
text = file.readline()

matches = re.findall(r"(?:XYZ)+(?:X|XY|XYZ)?", text)
print(len(max(matches, key=len)))
