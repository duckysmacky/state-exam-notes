def find(start, end, buff):
    if "****" in buff or "--" in buff: return 0
    if start > end: return 0
    if start == end: return 1
    return find(start - 1, end, buff + '-') + find(start * 2, end, buff + '*') + find(start * 3, end, buff + '*')
print(find(4, 166, ""))