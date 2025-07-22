import string

def base(x, p):
    num = ''
    while x > 0:
        num += str(x % p)
        x //= p
    return num[::-1]

alph = string.digits + string.ascii_uppercase
p = 22
for x in alph[:p]:
    val = int(f"5AG{x}2", p) + int(f"6{x}2{x}7", p)
    val9 = base(val, 9)
    if val9.count('7') == 2:
        print(x, val)
