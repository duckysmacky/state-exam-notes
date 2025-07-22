file = open("4.txt")
n = int(file.readline())
to_polish, to_paint = [], []
for i in range(n):
    polish, paint = map(int, file.readline().split())
    if polish < paint:
        to_polish.append((polish, i + 1))
    else:
        to_paint.append((paint, i + 1))
# print(to_polish, to_paint)
print(max(to_polish), max(to_paint))
print(len(to_polish))
# 9846 5032
