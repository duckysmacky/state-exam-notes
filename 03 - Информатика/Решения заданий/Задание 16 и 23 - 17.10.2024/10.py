def find(start, end):
    if start == 35: return 0
    if start > end: return 0
    if start == end: return 1
    return find(start + 1, end) + find(start * 3, end) + find(start * 4, end)
print(find(3, 10) * find(10, 70))