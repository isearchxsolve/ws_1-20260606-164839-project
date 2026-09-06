import numpy as np

def distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

def nearest_neighbor(points, start):
    tour = [start]
    unvisited = set(points)
    unvisited.remove(start)
    while unvisited:
        current = tour[-1]
        next_point = min(unvisited, key=lambda point: distance(point, current))
        tour.append(next_point)
        unvisited.remove(next_point)
    return tour

points = [(0, 0), (0, 2), (2, 2), (2, 0), (1, 1)]
start = points[0]
tour = nearest_neighbor(points, start)
print(tour)
