file = open("Задание 24/24.txt")
text = file.readline()

lines = []
buff = ""
i, j = 0, 0
while j < len(text):
    if text[i] == text[j]:
        buff += text[j]
    else:
        i = j
        if len(buff) > 0:
            lines.append(buff)
        buff = text[i]
    j += 1
print(lines, len(max(lines, key=len)))
