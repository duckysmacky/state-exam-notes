file = open("6.txt")
text = file.readline()
text = text.replace("YYZX", "YYZ YZX")
print(len(max(text.split(), key=len)))