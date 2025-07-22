from math import dist
from turtle import *

def draw_grid(k: int):
    for x in range(-10, 10):
        for y in range(-10, 10):
            setpos(x * k, y * k)
            dot()
    penup()
    setpos(-10 * k, 0)
    pendown()
    forward(20 * k)
    penup()
    setpos(0, -10 * k)
    left(90)
    pendown()
    forward(20 * k)
    penup()

def draw_clusters(k: int, clusters: list):
    colors = ["red", "blue", "green"]
    for i in range(len(clusters)):
        for x, y, b in clusters[i]:
            setpos(x * k, y * k)
            dot(5, colors[i])

def get_clusters(k, points):
    clusters = [[] for _ in range(k)]
    for x, y, b in points:
        if y > 0:
            clusters[0].append((x, y, b))
        elif x > 0.5:
            clusters[1].append((x, y, b))
        else:
            clusters[2].append((x, y, b))
    return clusters

def find_centroid(cluster):
    centroid_dist = []
    for cx, cy, cb in cluster:
        sum_dist = sum(dist((cx, cy), (x, y)) for x, y, b in cluster)
        centroid_dist.append((sum_dist, (cx, cy, cb)))
    return min(centroid_dist)[1]

def avg(cluster):
    br = [b for x, y, b in cluster]
    return sum(br) / len(br)

file = open("27B.txt")
file.readline()
points = [list(map(float, line.replace(',', '.').split())) for line in file]
k = 3

tracer(0)
screensize(2000, 2000)
penup()

clusters = get_clusters(k, points)
centroids = [find_centroid(cluster) for cluster in clusters]
average = [avg(cluster) for cluster in clusters]

P_xy = sum(x + y for x, y, b in centroids) / len(centroids)
P_m = sum(average)
print(int(P_xy * 10_000), int(P_m * 10_00))

draw_grid(20)
draw_clusters(20, clusters)

done()
