from re import findall

file = open("3.txt")
text = file.readline()

num = r"[789][0789]*"
pat = rf"{num}(?:[*]{num})*"
matches = findall(pat, text)

val = max(matches, key=eval)
print(val)
print(eval(val))
