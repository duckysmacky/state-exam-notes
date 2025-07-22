import re

def find_divs(x):
    divs = []
    for div in range(2, int(x ** 0.5) + 1):
        if div * div == x:
            divs.append(div)
        elif x % div == 0:
            divs.append(div)
            divs.append(x // div)
    return divs

pattern = r"[1-9]*2\d{2}2[0-9]*"

nums = []
for num in range(1, 100000):
    num = num ** 2
    if num > 10 ** 7:
        break
    divs = find_divs(num)
    if re.match(pattern, str(num)) and len(divs) % 2 != 0:
        nums.append(num)
print(max(nums) - min(nums))