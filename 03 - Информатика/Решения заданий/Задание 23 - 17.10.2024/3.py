def find(start, end):
    if start > end: return 0
    if start == end: return 1
    return find(start + 2, end) + find(start * 3, end) + find(start ** 2, end)
print(find(3, 77))