D = range(28, 70)
C = range(40, 92)
A = []
for x in range(1, 100):
    f = ((x in D) <= ((x not in C) and (x not in A))) <= (x not in D)
    if not f:
        A.append(x)
print(A)
