from re import findall

def is_zero(expr: str) -> bool:
    try:
        return eval(expr) == 0
    except Error:
        return False

def check(val: str) -> bool:
    return all(is_zero(x) for x in val.split('+'))

file = open("4.txt")
text = file.readline()

num = r"(?:0|[1-9]\d*)"
mult = rf"(?:{num}(?:\*{num})+)"
pat = rf"{mult}+(?:\+{mult})*"
matches = findall(pat, text)
valid = list(filter(check, matches))
best = max(valid, key=len)
print(best)
print(len(best))
