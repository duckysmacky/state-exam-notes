file = open("1/27B.txt")
file.readline()


def get_dist(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


clusters = [[], [], []]
for line in file:
    x, y = map(float, line.replace(',', '.').split())
    if x < 0:
        clusters[0].append((x, y))
    elif y > -4.5:
        clusters[1].append((x, y))
    else:
        clusters[2].append((x, y))

centroids = [(), (), ()]
for i in range(len(clusters)):
    min_dist_sum = 10 ** 10
    for cx, cy in clusters[i]:
        dist_sum = 0
        for x, y in clusters[i]:
            dist_sum += get_dist(cx, cy, x, y)
        if dist_sum < min_dist_sum:
            min_dist_sum = dist_sum
            centroids[i] = (cx, cy)

P_x = int((sum(x for x, y in centroids) / len(centroids)) * 10_000)
P_y = int((sum(y for x, y in centroids) / len(centroids)) * 10_000)
print(P_x, P_y)