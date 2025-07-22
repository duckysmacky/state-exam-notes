file = open("2.txt")
text = file.readline()
for letter in ['A', 'B', 'C']:
    text = text.replace(letter, 'a')
for number in ['6', '7', '8', '9']:
    text = text.replace(number, 'b')
while "aa" in text:
    text = text.replace("aa", "a a")
while "bb" in text:
    text = text.replace("bb", "b b")
text = text.split()
print(len(max(text, key=len)))