file = open('1.txt')
text = file.readline()

indexes = [i for i in range(len(text)) if text[i] == 'K']

step = 310 - 1
chars = []
for i in range(len(indexes) - step):
    chars.append(indexes[i + step] - indexes[i] + 1)
print(min(chars))