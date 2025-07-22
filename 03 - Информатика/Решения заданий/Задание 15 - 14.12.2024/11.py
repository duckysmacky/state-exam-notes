Q = range(47, 72)
P = range(25, 56)
R = range(40, 55)
A = []
for x in range(1, 100):
    f = (((x in P) <= (x not in Q)) and ((x in Q) <= (x in R)))
    if not f:
        A.append(x)
for a in A:
    if a in R:
        A.remove(a)
print(A)
