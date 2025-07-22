P = range(10, 15 + 1)
Q = range(14, 40 + 1)
A = []
for x in range(100):
    f = not ((x not in P) or (x not in Q)) and (x not in A)
    if not f == 0:
        A.append(x)
print(A)
print(15 - 14)