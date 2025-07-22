import string

def f(x, y):
    return int(f"13{y}{x}9", p) + int(f"22{y}22", p)

alph = string.digits + string.ascii_uppercase
p = 23
for x in alph[:p]:
    for y in alph[:p]:
        val = f(x, y)
        if val % 2 != 0: break
    else:
        val = f(x, 6)
        print(x, val // 18)
