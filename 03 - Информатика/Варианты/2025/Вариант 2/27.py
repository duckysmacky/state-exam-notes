from math import dist

def get_clusters(k: int, points: list) -> list:
    clusters = [[] for _ in range(k)]
    for x, y in points:
        if x > 0:
            clusters[0].append((x, y))
        elif y > 0:
            clusters[1].append((x, y))
        else:
            clusters[2].append((x, y))
    return clusters

def find_centroid(cluster: list) -> tuple:
    centroid_distances = []
    for centroid in cluster:
        distances = [dist(centroid, point) for point in cluster]
        centroid_distances.append((sum(distances), centroid))
    return min(centroid_distances)[1]

file = open("27var2B.csv")
points = [tuple(map(float, line.split(','))) for line in file]
k = 3

clusters = get_clusters(k, points)
centroids = [find_centroid(cluster) for cluster in clusters]

P_x = sum(x for x, y in centroids) / len(centroids)
P_y = sum(y for x, y in centroids) / len(centroids)
print(abs(int(P_x * 10_000)), abs(int(P_y * 10_000)))
