file = open("6.txt")
text = file.readline()
text = text.replace("YYZX", "YYZ YZX").split()
print(len(max(text, key=len)))