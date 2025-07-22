import math


def generate_centroids(k_clusters: int, points: int) -> list:
    centroids = [points[0]]
    for _ in range(k_clusters - 1):
        point_distances = []
        for point in points:
            distances = [math.dist(point, centroid) for centroid in centroids]
            point_distances.append((min(distances), point))
        centroids.append(max(point_distances)[1])
    return centroids


def find_centroid(cluster: list) -> tuple:
    centroid_distances = []
    for centroid in cluster:
        distances = [math.dist(centroid, point) for point in cluster]
        centroid_distances.append((sum(distances), centroid))
    return min(centroid_distances)[1]


def k_means(k_clusters: int, points: list, max_iterations: int = 10_000) -> list:
    centroids = generate_centroids(k_clusters, points)
    for _ in range(max_iterations):
        clusters = [[] for _ in range(k_clusters)]
        for point in points:
            closest = min(range(k_clusters), key=lambda i: math.dist(point, centroids[i]))
            clusters[closest].append(point)
        new_centroids = []
        for cluster in clusters:
            avg_x = sum(x for x, y in cluster) / len(cluster)
            avg_y = sum(y for x, y in cluster) / len(cluster)
            new_centroids.append((avg_x, avg_y))
        if new_centroids == centroids:
            break
        centroids = new_centroids
    return [find_centroid(cluster) for cluster in clusters]

file = open("1/27B.txt")
file.readline()

points = [tuple(map(float, line.replace(',', '.').split())) for line in file.readlines()]
centroids = k_means(3, points)

P_x = sum(x for x, y in centroids) / len(centroids)
P_y = sum(y for x, y in centroids) / len(centroids)
print(int(P_x * 10_000), int(P_y * 10_000))