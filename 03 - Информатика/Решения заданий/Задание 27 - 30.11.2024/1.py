import math


def find_clusters(k_clusters: int, points: list) -> list:
    clusters = [[] for _ in range(k_clusters)]
    for x, y in points:
        if x > 5:
            clusters[0].append((x, y))
        elif y > 0:
            clusters[1].append((x, y))
        else:
            clusters[2].append((x, y))
    return clusters


def find_centroid(cluster: int) -> tuple:
    centroid_distances = []
    for centroid in cluster:
        distances = [math.dist(centroid, point) for point in cluster]
        centroid_distances.append((sum(distances), centroid))
    return min(centroid_distances)[1]


file = open("1/27B.txt")
file.readline()
points = [tuple(map(float, line.replace(",", '.').split())) for line in file]
k = 3

clusters = find_clusters(k, points)
centroids = [find_centroid(cluster) for cluster in clusters]
P_x = sum(x for x, y in centroids) / len(centroids)
P_y = sum(y for x, y in centroids) / len(centroids)
print(int(P_x * 10_000), int(P_y * 10_000))