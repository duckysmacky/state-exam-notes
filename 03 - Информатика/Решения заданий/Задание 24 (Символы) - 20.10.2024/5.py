file = open("5.txt")
text = file.readline()

# 2
# aaaaXZaaXZaaaaaXZaaaXZ
# 0123456789
# 8 - 4 = 4 + 2 = 6

indexes = []
for i in range(len(text)):
    if text[i:i + 2] == "XZ":
        indexes.append(i)

step = 29 - 1
amounts = []
for i in range(len(indexes) - step):
    amounts.append(indexes[i + step] - indexes[i] + 2)
print(min(amounts))