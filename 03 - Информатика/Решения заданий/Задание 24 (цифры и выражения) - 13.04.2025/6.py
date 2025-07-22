import re

file = open("6.txt")
text = file.readline()

num = r"(?:0|[1-9]\d*)"
pattern = fr"{num}(?:[+*]{num})*"
matches = re.findall(pattern, text)

max_expr = ''
for sums in matches:
    expr = ''

    for mults in sums.split('+'):
        if len(mults) > 0:
            if eval(mults) == 0:
                expr += mults + '+'
            else:
                if '0*' in mults:
                    i = mults.index('0*')
                    expr = mults[i:] + '+'
                elif mults[-1] == '0':
                    expr = '0+'
                else:
                    expr = ''
        else:
            expr = ''
        max_expr = max(max_expr, expr, key=len)
print(max_expr, len(max_expr) - 1)
