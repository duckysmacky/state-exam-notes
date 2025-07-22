from re import findall

file = open("2.txt")
text = file.readline()

num = r"[2-4][0-4]*"
pat = rf"{num}(?:[+*]{num})*"
matches = findall(pat, text)

val = max(matches, key=len)
print(val)
print(len(val))
