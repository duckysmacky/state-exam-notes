import math


def split_clusters(k: int, points: list) -> list:
    clusters = [[] for _ in range(k)]
    for x, y in points:
        if y > 8 and x < 4:
            continue
        elif y > 8 and x > 10:
            continue
        elif y < -2 and x > 9:
            continue
        elif 2 < y < 7 and 5 < x < 8:
            clusters[0].append((x, y))
        elif y < 6 and x < 8:
            clusters[1].append((x, y))
        else:
            clusters[2].append((x, y))
    return clusters


def find_centroid(cluster: list) -> tuple:
    centroid_distances = []
    for centroid in cluster:
        distances = [math.dist(centroid, point) for point in cluster]
        centroid_distances.append((sum(distances), centroid))
    return min(centroid_distances)[1]


file = open("3/27B.txt")
file.readline()
k = 3
points = [tuple(map(float, line.replace(',', '.').split())) for line in file]

clusters = split_clusters(k, points)
centroids = [find_centroid(cluster) for cluster in clusters]
p_x = sum(x for x, y in centroids) / len(centroids)
p_y = sum(y for x, y in centroids) / len(centroids)
print(int(p_x * 10_000), int(p_y * 10_000))