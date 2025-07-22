file = open("2.txt")
text = file.readline()
text = text.split('Y')
print(len(max(text, key=len)))