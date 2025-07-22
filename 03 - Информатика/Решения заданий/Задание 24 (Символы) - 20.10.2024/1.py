file = open("1.txt")
text = file.readline()
text = text.replace('A', '*').replace('B', '*').replace('C', '*')
while "**" in text:
    text = text.replace("**", "* *")
text = text.split()
print(len(max(text, key=len)))