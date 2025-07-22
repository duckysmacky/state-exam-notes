Q = range(6, 15)
P = range(2, 11)
A = list(range(1, 100))
for x in range(1, 100):
    f = ((x in A) <= (x in P)) or (x in Q)
    if not f:
        A.remove(x)
print(A)
