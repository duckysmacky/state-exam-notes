Q = range(21, 58)
P = range(3, 39)
A = list(range(1, 100))

for x in range(1, 100):
    f = ((x in Q) <= (x in P)) <= (x not in A)
    if not f:
        A.remove(x)

print(A)
