file = open("6.txt")
text = "BE" + file.readline() + "BE"

# 2
# BEaaaBEaBEaaaBE -> 13
# 0123456789...(13)
# 13 - 0 = 13

indexes = []
for i in range(len(text)):
    if text[i:i + 2] == "BE":
        indexes.append(i)

step = 16 + 1
amounts = []
for i in range(len(indexes) - step):
    amounts.append(indexes[i + step] - indexes[i])
print(max(amounts))