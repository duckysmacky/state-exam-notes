file = open('3.txt')
text = file.readline()

chars = []
for substr in text.split('E'):
    if substr.count('C') <= 300:
        chars.append(len(substr))
    else:
        substr = 'C' + substr + 'C'
        indexes = [i for i in range(len(substr)) if substr[i] == 'C']

        step = 300 + 1
        for i in range(len(indexes) - step):
            chars.append(indexes[i + step] - indexes[i] - 1)
print(max(chars))