file = open("5.txt")
text = file.readline()
text = text.replace("ANT", "AN NT")
text = text.replace("AN", "*").replace("NT", "*")
for n in range(100):
    if "*" * n in text:
        print(n)