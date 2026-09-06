import unittest
from src.main import nearest_neighbor

class TestNearestNeighbor(unittest.TestCase):
    def test_tour(self):
        points = [(0, 0), (0, 2), (2, 2), (2, 0), (1, 1)]
        start = points[0]
        tour = nearest_neighbor(points, start)
        self.assertEqual(tour, [(0, 0), (0, 2), (2, 2), (2, 0), (1, 1)])

if __name__ == '__main__':
    unittest.main()
