import string

alph = string.digits + string.ascii_uppercase
for x in alph[:23]:
    val = int(f'1{x}1{x}1{x}1{x}1', 23) + int(f'20{x}24', 23) + int(f'1{x}235', 23)
    if val % 22 == 0:
        print(x, val // 22)
        break
