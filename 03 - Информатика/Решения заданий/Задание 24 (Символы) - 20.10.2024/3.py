file = open("3.txt")
text = file.readline()

indexes = []
for i in range(len(text)):
    if text[i] == 'K':
        indexes.append(i)

step = 310 - 1
amounts = []
for i in range(len(indexes) - step):
    amounts.append(indexes[i + step] - indexes[i] + 1)
print(min(amounts))