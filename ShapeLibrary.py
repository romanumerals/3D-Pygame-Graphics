import Geometry
from Geometry import Point

# objects

class Cube:

	def __init__(self, cx, cy, cz, side_length):
		add = side_length / 2
		# ---all--- shapes are stored as a list of verteces and a list of edges between two verteces
		self.verteces = [Point(cx+add, cy+add, cz+add),
						Point(cx+add, cy+add, cz-add),
						Point(cx+add, cy-add, cz+add),
						Point(cx+add, cy-add, cz-add),
						Point(cx-add, cy+add, cz+add),
						Point(cx-add, cy+add, cz-add),
						Point(cx-add, cy-add, cz+add),
						Point(cx-add, cy-add, cz-add),]
		self.edge = [(0, 1), (0, 4), (0, 2), (1, 3), (1, 5), (2, 6), (2, 3), (3, 7), (4, 5), (4, 6), (5, 7), (6, 7)]
		self.center = Point(cx, cy, cz)

class TriangleBasedPyramid:

        def __init__(self, points):
                self.verteces = points
                self.edge = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
                self.center = points[0]