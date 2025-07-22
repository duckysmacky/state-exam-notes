file = open("Задание 24/24.txt")
text = file.readline()
text = text.split('A')
max_len = 0
for i in range(len(text) - 1):
    max_len = max(max_len, len(text[i] + 'A' + text[i + 1]))
print(max_len)