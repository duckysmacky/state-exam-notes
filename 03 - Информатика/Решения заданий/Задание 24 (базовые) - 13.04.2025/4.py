file = open('4.txt')
text = file.readline()
text = text.replace('ZYX', 'ZXY')
for i in range(100):
    if 'ZXY' * i in text:
        print(i)