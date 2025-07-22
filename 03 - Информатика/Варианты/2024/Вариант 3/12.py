s = '>' + '2' * 15 + '3' * 20 + '5' * 25
while ">2" in s or ">3" in s or ">5" in s:
    if ">2" in s:
        s = s.replace(">2", "333>", 1)
    if ">3" in s:
        s = s.replace(">3", "23>", 1)
    if ">5" in s:
        s = s.replace(">5", "35>", 1)
print(sum(map(int, s.replace('>', ''))))