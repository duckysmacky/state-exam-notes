import re
from itertools import permutations

file = open("Задание 24/24.txt")
text = file.readline()

pattern = re.compile("[ABCD]+[ABCD]+[ABCD]+[ABCD]+")

text = re.split(pattern, text)
print(len(max(text, key=len)))