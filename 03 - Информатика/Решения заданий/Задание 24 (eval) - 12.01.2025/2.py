file = open("2.txt")
max_val = 0
for line in file:
    try:
        val = int(eval(line))
        max_val = max(max_val, val)
    except (SyntaxError, NameError): pass
print(max_val)