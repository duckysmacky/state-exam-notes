P = range(13, 21 + 1)
Q = range(23, 35 + 1)
R = range(28, 38 + 1)
A = []
for x in range(1, 100):
    f = (not ((x in Q) <= ((x in P) or (x in R)))) <= ((not (x in A)) <= (not (x in Q)))
    if not f:
        A.append(x)
print(A)
print(28 - 23)
