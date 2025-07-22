file = open("24.txt")
text = 'AB' + file.readline() + 'AB'
# text = "ABaaaABaaaaaABaaABaAB"

indexes = [i for i in range(len(text) - 1) if text[i:i + 2] == 'AB']

step = 21 - 1
cnts = []
for i in range(len(indexes) - step):
    cnts.append(indexes[i + step] - indexes[i])
print(min(cnts) + 2)
