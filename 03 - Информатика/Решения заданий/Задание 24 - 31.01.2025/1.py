file = open("1.txt")
symb = "RO"
text = symb + file.readline() + symb

indexes = [i for i in range(len(text) - 1) if text[i:i + 2] == symb]

cnt = 2 + 1
substrs = []
for i in range(len(indexes) - cnt):
    substrs.append(indexes[i + cnt] - indexes[i])

print(substrs)
print(max(substrs))
