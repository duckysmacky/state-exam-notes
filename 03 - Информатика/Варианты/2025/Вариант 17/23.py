def find(s, e, cnt):
    if s == e: return cnt == 7
    if s > e: return 0
    return find(s + 1, e, cnt + 1) + find(s + 4, e, cnt + 1) + find(s * 2, e, cnt + 1)

print(find(3, 27, 0))
