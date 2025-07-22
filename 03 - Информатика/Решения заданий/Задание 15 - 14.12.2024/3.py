Q = range(12, 22 + 1)
P = range(3, 13 + 1)
A = list(range(1, 100))
for x in range(1, 100):
    f = ((x in A) <= (x in P)) or (x in Q)
    if not f:
        A.remove(x)
print(A)
print(22 - 3)
