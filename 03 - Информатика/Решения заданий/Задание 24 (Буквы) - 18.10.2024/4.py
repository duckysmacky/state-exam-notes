file = open("4.txt")
text = file.readline()
text = text.replace("ZXY", "*").replace("ZYX", "*")
for n in range(1000):
    if "*" * n in text: print(n)
    else: break