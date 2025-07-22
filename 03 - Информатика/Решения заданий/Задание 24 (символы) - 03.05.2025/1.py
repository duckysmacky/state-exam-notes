file = open('1.txt')
text = 'N' + file.readline() + 'N'

indexes = [i for i in range(len(text)) if text[i] == 'N']

step = 159 + 1
chars = []
for i in range(len(indexes) - step):
    chars.append(indexes[i + step] - indexes[i] - 1)
print(max(chars))