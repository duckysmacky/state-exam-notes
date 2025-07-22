def find(start, end):
    if start > end: return 0
    if start == end: return 1
    return find(start + 1, end) + find(start + 10, end)
print(find(12, 27))