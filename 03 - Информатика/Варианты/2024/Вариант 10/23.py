def find(start, end, hist):
    if start == 33: return 0
    if "22" in hist: return 0
    if start > end: return 0
    if start == end: return 1
    return find(start + 1, end, hist + "1") \
        + find(start + 3, end, hist + "3") \
        + find(start * 2, end, hist + "2")

print(find(2, 18, '') * find(18, 51, ''))
