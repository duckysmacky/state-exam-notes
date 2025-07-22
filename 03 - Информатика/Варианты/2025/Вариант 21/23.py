def find(s, e):
    if s > e: return 0
    if '7' in str(s): return 0
    if s == e: return 1
    return find(s + 1, e) + find(s + 7, e)

print(find(1, 61))