file = open('24.txt')
text = file.readline()
# text = 'A*****A***A****A*****A**A***A***A*****A***A**A***A**A'

indexes = [i for i in range(len(text)) if text[i] == 'A']
step = 2024 - 1
cnts = []
for i in range(len(indexes) - step):
    cnts.append(indexes[i + step] - indexes[i] + 1)
print(min(cnts))
