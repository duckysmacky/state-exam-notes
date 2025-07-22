with open("Задание 26/26.txt", "r") as f:
	n = int(f.readline())
	data = [(int(x.split()[0]), int(x.split()[1])) for x in f.readlines()]

maxr = max([x[0] for x in data])
maxc = max([x[1] for x in data])

lab = [[0 for _ in range(maxc)] for _ in range(maxr)]

for x in data:
	lab[x[0] - 1][x[1] - 1] = 1

for row in range(len(lab)):
	flag = False
	c = 0
	for elem in range(len(lab[row])):
		if lab[row][elem] == 0: c += 1
		elif c == 14:
			flag = True
			break
		else:
			c = 0
	if flag:
		print(row + 1, elem + 1 - 14)
		break
