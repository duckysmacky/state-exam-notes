file = open("1.txt")
n, places_n, rows_n = map(int, file.readline().split())

places = [rows_n] * (places_n + 1)
for line in file:
    row, place = map(int, line.split())
    places[place] = min(places[place], row - 1)

ans = []
for i in range(1, len(places) - 1):
    ans.append((min(places[i], places[i + 1]), -i, -(i + 1)))
ans.sort(reverse=True)
print(ans[:10])
