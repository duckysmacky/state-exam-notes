file = open("Задание 26/26.txt")
N = int(file.readline())
coords = [list(map(int, line.split())) for line in file]
# print(coords)

for i in range(len(coords) - 1):
    if coords[i][0] == coords[i + 1][0]:
        print(coords[i], coords[i + 1])
        if abs(coords[i][1] - coords[i + 1][1]) - 1 == 14:
            print(coords[i][0], coords[i][1] + 1)