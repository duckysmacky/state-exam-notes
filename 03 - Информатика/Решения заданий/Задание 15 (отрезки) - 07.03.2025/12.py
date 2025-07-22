Q = range(33, 89)
P = range(10, 50)
A = list(range(1, 100))
for x in range(1, 100):
    f = ((x in P) <= (x not in Q)) <= (x not in A)
    if not f:
        A.remove(x)
print(A)
