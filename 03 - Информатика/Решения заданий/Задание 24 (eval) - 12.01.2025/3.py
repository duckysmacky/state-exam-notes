import re

file = open("3.txt")
max_val = 0
test = "-213*121+121-5*3"

def clear(exp: str) -> str:
    exp = re.sub(r"-\d+", '', exp)
    if exp[0] in "+*":
        exp = exp[1:]
    return exp

for line in file:
    try:
        val = eval(clear(line))
        max_val = max(max_val, val)
    except (NameError, SyntaxError): pass
print(max_val)