file = open("4.txt")
text = 'O' + file.readline() + 'O'

indexes = []
for i in range(len(text)):
    if text[i] == 'O':
        indexes.append(i)

step = 150 + 1
amounts = []
for i in range(len(indexes) - step):
    amounts.append(indexes[i + step] - indexes[i] - 1)
print(max(amounts))