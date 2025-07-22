import re

file = open("24.txt")
text = file.readline()
pattern = r"[^D]ANOV|D[^A]NOV|DA[^N]OV|DAN[^O]V|DANO[^V]"

substrs = re.split(pattern, text)
best = max(substrs, key=len)
i = text.index(best)
print(len(best), text[i - 5:i + 5], text[i + len(best):i + len(best) + 5])
print(len(best) + 4)
