x = '>' + 32 * '1' + 11 * '4' + 22 * '6'

while ">1" in x or ">4" in x or ">6" in x:
    if ">1" in x:
        x = x.replace(">1", "1661>", 1)
    if ">4" in x:
        x = x.replace(">4", "146141>", 1)
    if ">6" in x:
        x = x.replace(">6", "141>", 1)

print(sum([int(n) for n in x if n.isdigit()]))
