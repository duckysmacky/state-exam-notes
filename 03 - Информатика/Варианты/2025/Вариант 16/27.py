from math import dist
from turtle import *

def draw(clusters):
    colors = ['red', 'green', 'blue', 'yellow']
    k = 20
    penup()
    tracer(0)
    screensize(2000, 2000)

    for i in range(len(clusters)):
        for x, y in clusters[i]:
            setpos(x * k, y * k)
            dot(5, colors[i])

    done()

def get_clusters(points, eps):
    clusters = []
    while len(points) > 0:
        clusters.append([points.pop(0)])
        for origin_point in clusters[-1]:
            for point in points[:]:
                if dist(origin_point, point) < eps:
                    clusters[-1].append(point)
                    points.remove(point)
        if len(clusters[-1]) <= 10:
            clusters.pop(-1)
    return clusters

def find_centroid(cluster):
    centroid_dists = []
    for centroid in cluster:
        sum_dists = sum(dist(centroid, point) for point in cluster)
        centroid_dists.append((sum_dists, centroid))
    return min(centroid_dists)[1]

file = open("27B.txt")
points = [tuple(map(float, line.split())) for line in file]

clusters = get_clusters(points, 0.5)
centroids = [find_centroid(cluster) for cluster in clusters]

P_x = sum(x for x, y in centroids) / len(centroids)
P_y = sum(y for x, y in centroids) / len(centroids)
form = lambda x: int(abs(x) * 10_000)
print(form(P_x), form(P_y))

draw(clusters)
