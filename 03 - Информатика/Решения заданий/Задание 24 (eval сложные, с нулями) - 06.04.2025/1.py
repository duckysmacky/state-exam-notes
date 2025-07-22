import re

file = open('1.txt')
text = "58*855*0++730+0*71*82+0+0*234++560*72"
text = file.readline()

num = r"(?:0|[1-9][0-9]*)"
pattern = fr"{num}(?:[+*]{num})*"
exprs = re.findall(pattern, text)

max_arithm = ''
for expr in exprs:
    arithm = ''
    psums = expr.split('+')

    for psum in psums:
        if len(psum) > 0 and eval(psum) == 0:
            arithm += psum + '+'
        elif len(psum) > 0:
            if '0*' in psum:
                arithm = psum[psum.index('0*'):] + '+'
            elif psum[-1] == '0':
                arithm = '0*'
            else:
                arithm = ''
        else:
            arithm = ''
        max_arithm = max(max_arithm, arithm, key=len)

print(len(max_arithm) - 1)