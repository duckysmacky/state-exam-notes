file = open("1.txt")
text = file.readline()
for i in range(100):
    if "B" * i in text:
        print(i)