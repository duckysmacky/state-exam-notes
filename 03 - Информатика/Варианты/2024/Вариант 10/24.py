file = open("24.txt")
text = file.readline()
letters = {}
for i in range(len(text) - 1):
    if text[i] == 'X':
        l = text[i + 1]
        letters[l] = letters.get(l, 0) + 1

maxl = max(letters, key=letters.get)
print(f"{maxl}{letters[maxl]}")
