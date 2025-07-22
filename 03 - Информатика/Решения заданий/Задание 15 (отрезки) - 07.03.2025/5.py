Q = range(20, 39)
P = range(7, 16)
A = list(range(1, 100))

for x in range(1, 100):
    f = ((x not in P) <= (x in Q)) or (x not in A)
    if not f:
        A.remove(x)

print(A)
