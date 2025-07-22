file = open("1.txt")
text = file.readline()
for n in range(1000):
    if 'B' * n in text:
        print(n)