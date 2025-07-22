file = open("27A_1.txt")
file.readline()
points = [list(map(float, line.replace(",", ".").split())) for line in file]

def euclidean_dist(point_a: list, point_b: list) -> float:
    x1, y1 = point_a
    x2, y2 = point_b
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

min_sum_dist = 10 ** 10
best_centroids = ()
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        centroid1, centroid2 = points[i], points[j]
        sum_dist = 0
        for point in points:
            dist1 = euclidean_dist(centroid1, point)
            dist2 = euclidean_dist(centroid2, point)
            sum_dist += min(dist1, dist2)
        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            best_centroids = (centroid1, centroid2)

P_x = int((sum(x for x, y in best_centroids) / 2) * 10_000)
P_y = int((sum(y for x, y in best_centroids) / 2) * 10_000)

print(P_x, P_y)