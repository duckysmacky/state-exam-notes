import re

file = open('1.txt')
text = file.readline()

pattern = f"[1-9][0-9A]*"
nums = re.findall(pattern, text)
print(len(max(nums, key=len)))