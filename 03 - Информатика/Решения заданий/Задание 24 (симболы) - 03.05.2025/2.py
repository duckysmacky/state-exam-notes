file = open('2.txt')
text = file.readline()
text = 'O' + text + 'O'

indexes = [i for i in range(len(text)) if text[i] == 'O']
step = 150 + 1
chars = []
for i in range(len(indexes) - step):
    chars.append(indexes[i + step] - indexes[i] - 1)
print(max(chars))