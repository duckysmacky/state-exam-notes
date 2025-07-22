file = open('5.txt')
text = file.readline()

text = 'abc^de$f#g^hi$jkl#m^no$pqrs^$t#u^vw$xyz#a$bcd^efgh'

substrs = []
i, j = 0, 0
while i < len(text):
    substr = text[i:j + 1]
    if substr.count('^') + substr.count('$') == 2 and substr.count('#') <= 1:
        print(i, j, substr, 'good')
        substrs.append(substr)
    else:
        print(i, j, substr, 'bad')
    if j >= len(text):
        i += 1
        j = i
    j += 1
best = max(substrs, key=len)
print(best, len(best))