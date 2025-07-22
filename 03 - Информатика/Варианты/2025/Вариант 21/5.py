def get_letters(num: str):
    letters = sorted(list(num))
    return letters[0], letters[-1]

def alg(n):
    n16 = hex(n)[2:]
    if n % 2 == 0:
        n16 += 'f'
    else:
        n16 += '0'
    n16 += hex(sum(map(lambda x: int(x, 16), n16)) % 16)[2:]
    n16 += hex(sum(map(lambda x: int(x, 16), n16)) % 16)[2:]
    return n16

for n in range(10000):
    R = alg(n)
    minl, maxl = get_letters(R)
    if R.count(maxl) * 5 == R.count(minl):
        print(n, R)
        break