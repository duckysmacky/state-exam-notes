P = range(13, 38)
Q = range(22, 52)
A = []

def DEL(n: int, m: int) -> bool: return n % m == 0

for x in range(1, 100):
    f = ((x in Q) <= (DEL(x, 18) or (x in P))) <= (x in A)
    if f: A.append(x)
print(A)
