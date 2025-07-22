file = open("2.txt")
part_count = int(file.readline())
line_start, line_end = [], []
for i in range(part_count):
    polish_time, paint_time = map(int, file.readline().split())
    if polish_time < paint_time:
        line_start.append([polish_time, i + 1])
    else:
        line_end.append([paint_time, i + 1])
line_start.sort()
line_end.sort()
print(max(line_start), max(line_end))
print(len(line_start))