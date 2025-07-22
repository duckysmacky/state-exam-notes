from math import dist
from turtle import *

def draw(clusters):
    tracer(0), penup(), screensize(2000, 2000)
    k = 20
    colors = ["red", "green", "blue", "yellow"]

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
        dist_sum = sum(dist(centroid, point) for point in cluster)
        centroid_dists.append((dist_sum, centroid))
    return min(centroid_dists)[1]

file = open("27B.txt")
file.readline()
points = [list(map(float, line.replace(',', '.').split())) for line in file]

clusters = get_clusters(points, 0.3)
centroids = [find_centroid(cluster) for cluster in clusters]
areas = [len(cluster) / (4 * 4) for cluster in clusters]

P_x = sum(x for x, y in centroids) / len(centroids)
P_y = sum(y for x, y in centroids) / len(centroids)
P_s = sum(areas)
print(int((P_x + P_y) * 10_000), int(P_s * 1000))

draw(clusters)
