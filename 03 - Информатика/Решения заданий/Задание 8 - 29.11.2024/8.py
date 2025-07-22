from itertools import permutations

cnt = 0
for w in set(permutations("ДИАНА", r=5)):
    w = ''.join(w)
    if "АА" not in w:
        cnt += 1
print(cnt)