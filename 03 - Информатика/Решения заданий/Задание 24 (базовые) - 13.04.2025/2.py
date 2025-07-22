file = open("2.txt")
text = file.readline()
print(len(max(text.split("Y"), key=len)))