file = open("1.txt")
vals = []
for i, line in enumerate(file, 1):
	try:
		vals.append((eval(line), i))
	except SyntaxError: pass
print(sorted(vals, reverse=True)[:5])