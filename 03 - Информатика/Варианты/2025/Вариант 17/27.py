from math import dist
from turtle import *

def draw(clusters):
    k = 1
    tracer(0); screensize(2000, 2000); penup()
    colors = ["blue", "red", "yellow", "green"]

    for i in range(len(clusters)):
        for x, y, _ in clusters[i]:
            setpos(x * k, y * k)
            dot(5, colors[i])

    done()

def get_clusters(points, eps):
    clusters = []
    while len(points) > 0:
        clusters.append([points.pop(0)])
        for ox, oy, _ in clusters[-1]:
            for point in points[:]:
                x, y, _ = point
                if dist((ox, oy), (x, y)) < eps:
                    clusters[-1].append(point)
                    points.remove(point)
        if len(clusters[-1]) <= 10:
            clusters.pop(-1)
    return clusters

def find_centroid(cluster):
    centroid_dists = []
    for cx, cy, ch in cluster:
        sum_dists = sum(dist((cx, cy), (x, y)) * h for x, y, h in cluster)
        centroid_dists.append((sum_dists, (cx, cy, ch)))
    return min(centroid_dists)[1]

file = open("27-b.txt")
points = [tuple(map(float, line.split())) for line in file]

clusters = get_clusters(points, 50)
centroids = [find_centroid(cluster) for cluster in clusters]

P_x = sum(x for x, _, _ in centroids) / len(centroids)
P_y = sum(y for _, y, _ in centroids) / len(centroids)

draw(clusters)

print(int(P_x * 100_000), int(P_y * 100_000))
