P = range(7, 15 + 1)
Q = range(20, 38 + 1)
r = range(1, 100)
A = list(r)

for x in r:
    f = ((not (x in P)) <= (x in Q)) or not (x in A)
    if not f:
        A.remove(x)
print(A)
print(38 - 20)
