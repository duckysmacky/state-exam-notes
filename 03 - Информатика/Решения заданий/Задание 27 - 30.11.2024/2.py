import math


def split_clusters(k: int, points: list) -> list:
    clusters = [[] for _ in range(k)]
    for x, y in points:
        if x < -4:
            clusters[0].append((x, y))
        elif x < 2:
            clusters[1].append((x, y))
        elif y < -2:
            clusters[2].append((x, y))
        else:
            clusters[3].append((x, y))
    return clusters


def find_centroid(clusters: list) -> tuple:
    centoid_distances = []
    for centroid in clusters:
        distances = [math.dist(centroid, point) for point in clusters]
        centoid_distances.append((sum(distances), centroid))
    return min(centoid_distances)[1]


file = open("2/27B.txt")
file.readline()
k = 4
points = [tuple(map(float, line.replace(',', '.').split())) for line in file]

clusters = split_clusters(k, points)
centroids = [find_centroid(cluster) for cluster in clusters]
P_x = sum(x for x, y in centroids) / len(centroids)
P_y = sum(y for x, y in centroids) / len(centroids)
print(int(P_x * 10_000), int(P_y * 10_000))