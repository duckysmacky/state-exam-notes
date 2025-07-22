from math import dist
from turtle import *

def draw(clusters, k=20):
    tracer(0); screensize(2000, 2000); penup()
    colors = ['yellow', 'blue', 'red', 'green']
    for i in range(len(clusters)):
        for x, y in clusters[i]:
            setpos(x * k, y * k)
            dot(5, colors[i])
    done()

def get_clusters(points, eps):
    clusters = []
    while len(points) > 0:
        clusters.append([points.pop(0)])
        for origin in clusters[-1]:
            for point in points[:]:
                if dist(origin, point) < eps:
                    clusters[-1].append(point)
                    points.remove(point)
        if len(clusters[-1]) < 10:
            clusters.pop(-1)
    return clusters

def find_centroid(cluster):
    dists = []
    for centroid in cluster:
        dist_sum = sum(dist(centroid, point) for point in cluster)
        dists.append((dist_sum, centroid))
    return min(dists)[1]

file = open('27-b.txt')
points = [tuple(map(float, line.split())) for line in file]

clusters = get_clusters(points, 0.5)
centroids = [find_centroid(c) for c in clusters]

px = sum(x for x, y in centroids) / len(centroids)
py = sum(y for x, y in centroids) / len(centroids)
print(int(abs(px) * 10_000), int(abs(py) * 10_000))

draw(clusters)
