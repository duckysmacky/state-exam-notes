file = open("3.txt")
text = file.readline()
text = (text
        .replace("E", "g")
        .replace("I", "g")
        .replace("O", 'g')
        .replace('M', 's')
        .replace('K', 's'))
for i in range(100):
    if 'sg' * i in text:
        print(i)