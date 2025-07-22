from turtle import *
from math import dist

def draw(clusters):
    k = 20
    tracer(0); penup(); screensize(2000, 2000)
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
        if len(clusters[-1]) < 5:
            clusters.pop(-1)
    return clusters

def centroid(cluster):
    dists = []
    for centroid in cluster:
        sum_dists = sum(dist(centroid, point) for point in cluster)
        dists.append((sum_dists, centroid))
    return min(dists)[-1]

file = open("27B.txt")
file.readline()
points = [tuple(map(float, line.replace(',', '.').split())) for line in file]

clusters = get_clusters(points, 0.25)
centroids = [centroid(c) for c in clusters]

P_x = sum(x for x, y in centroids) / len(centroids)
P_y = sum(y for x, y in centroids) / len(centroids)
print(int(abs(P_x * 10_000)), int(abs(P_y * 10_000)))

draw(clusters)
