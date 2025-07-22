file = open("3.txt")
text = file.readline()
text = text.replace('E', 'a').replace('I', 'a').replace('O', 'a')
text = text.replace('M', 'b').replace('K', 'b')
for n in range(10000):
    if "ba" * n in text:
        print(n)
    else:
        break