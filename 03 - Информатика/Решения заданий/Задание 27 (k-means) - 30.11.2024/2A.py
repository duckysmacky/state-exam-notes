import math
import turtle as t

def avg_coords(values: list) -> tuple:
    avg_x = sum(x for x, y in values) / len(values)
    avg_y = sum(y for x, y in values) / len(values)
    return avg_x, avg_y


def generate_centroids(k_clusters: int, points: list) -> list:
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
            closest_i = min(range(k_clusters), key=lambda i: math.dist(point, centroids[i]))
            clusters[closest_i].append(point)
        new_centroids = [avg_coords(cluster) for cluster in clusters]
        if new_centroids == centroids:
            break
        centroids = new_centroids
    return [find_centroid(cluster) for cluster in clusters]


def draw_points(points: list) -> None:
    t.screensize(500, 500)
    t.tracer(0)
    t.penup()
    k = 20
    for x, y in points:
        t.setpos(x * k, y * k)
        t.dot()
    t.done()


file = open("2/27B.txt")
file.readline()
points = [tuple(map(float, line.replace(',', '.').split())) for line in file.readlines()]
draw_points(points)

centroids = k_means(3, points)
P_x, P_y = avg_coords(centroids)
print(int(P_x * 10_000), int(P_y * 10_000))