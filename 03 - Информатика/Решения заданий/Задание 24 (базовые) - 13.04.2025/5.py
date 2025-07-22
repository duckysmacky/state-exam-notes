file = open("5.txt")
text = file.readline()
text = text.replace("ANT", "AN NT").replace("AN", "NT")
for i in range(100):
    if "NT" * i in text:
        print(i)