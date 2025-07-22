def find(start, end):
    if start < end: return 0
    if start == end: return 1
    return find(start - 3, end) + find(int(start / 3), end)
print(find(81, 27) * find(27, 3))