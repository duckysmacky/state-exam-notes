from math import dist
from turtle import *

def draw_grid(k: int, size=10):
    for x in range(-size, size):
        for y in range(-size, size):
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

def draw_points(k: int, points: list):
    for x, y in points:
        setpos(x * k, y * k)
        dot()

def draw_clusters(k: int, clusters: list):
    colors = ["red", "green", "blue"]
    for i in range(len(clusters)):
        for x, y in clusters[i]:
            setpos(x * k, y * k)
            dot(5, colors[i])

def get_clusters(n: int, points: list) -> list:
    clusters = [[] for _ in range(n)]
    for x, y in points:
        if y < -1:
            clusters[0].append((x, y))
        elif x > 0:
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

file = open("27B.txt")
file.readline()
points = [list(map(float, line.replace(',', '.').split())) for line in file]

tracer(0)
screensize(2000, 2000)
penup()
k = 30

draw_grid(k)
#draw_points(k, points)

clusters = get_clusters(3, points)
draw_clusters(k, clusters)
centroids = [find_centroid(cluster) for cluster in clusters]

P_x = sum(x for x, y in centroids) / len(centroids)
P_y = sum(y for x, y in centroids) / len(centroids)
print(int(P_x * 10_000), int(P_y * 10_000))

done()
