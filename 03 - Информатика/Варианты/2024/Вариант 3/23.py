def find(start: int, end: int):
    if start > end: return 0
    if start == end: return 1
    return find(start + 1, end) + find(start * 3, end)

print(find(1, 11) * find(11, 34))