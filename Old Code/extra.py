# --- classes ---

class World:
	def __init__(self):
		self.objects = []

	def update(self):
		for i in objects:
			i.update

	def draw(self, camera):
		camera.draw(self.objects)

class Point:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def move(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def getPoint(self):
		return self.x, self.y, self.z

	def ifCollide(self, x, y, z):
		if self.x == x and self.y == y and self.z == z:
			return True
		return False

	def update():
		pass

class Line:
	def __init__(self, x1, y1, z1, x2, y2, z2):
		self.x1 = x1
		self.y1 = y1
		self.z1 = z1
		self.x2 = x2
		self.y2 = y2
		self.z2 = z2

	def getLine(self):
		return self.x1, self.y1, self.z1, self.x2, self.y2, self.z2

	def ifPointOnLine(self, x, y, z):
		screen1 = pointOnLine2D(x1, y1, x2, y2, x3, y3)
		screen2 = pointOnLine2D(x1, z1, x2, z2, x3, z3)
		screen3 = pointOnLine2D(y1, z1, y2, z2, y3, z3)

		if screen1 and screen2:
			return True

		elif screen1 and screen3:
			return True

		elif screen2 and screen3:
			return True

		return False

	def update():
		pass


# --- functions ---

def pointOnLine2D(x1, y1, x2, y2, x3, y3):
		dx = x2 - x1
		dy = y2 - y1
		m = dy / dx
		b = y1 - m

		if y3 == m*x3 + b and (x1 < x3 < x2 or x2 < x3 < x1):
			return True
		return False

def lineIntersect3D(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4):
	''' this function sees if two lines intersect, if they do, it returns the point, if not it returns none'''
	screen1 = lineIntersect2D(x1, y1, x2, y2, x3, y3, x4, y4)
	screen2 = lineIntersect2D(x1, z1, x2, z2, x3, z3, x4, z4)
	screen3 = lineIntersect2D(y1, z1, y2, z2, y3, z3, y4, z4)

	print(screen1)

	if bool(screen1) and bool(screen2):
		return (screen1[0], screen1[1], screen2[1])

	elif bool(screen1) and bool(screen3):
		return (screen1[0], screen1[1], screen3[1])

	elif bool(screen2) and bool(screen3):
		return (screen2[0], screen3[0], screen3[1])

	return None


def lineIntersect2D(x1, y1, x2, y2, x3, y3, x4, y4):
	dx1 = x2 - x1
	dy1 = y2 - y1
	m1 = dy1 / dx1

	dx2 = x4 - x3
	dy2 = y4 - y3
	m2 = dy2 / dx2

	if m1 == m2:
		# I don't deal with paralell lines - fuck that shit
		return None

	# black magic - do not touch

	# these equasions will give the x and y coordinates of the intersection any two intersecting lines that intersect
	# don't ask me how it works - i forgot and I am to lazy to do it again
	# note: it is on a peice of paper somwhere
	x_prime = (m1 * x2 + y3 - y1 - m2 * x4)/(m1-m2)
	y_prime = m1 * x_prime + y1 - m1 * x1
	print(x_prime, y_prime)

	# make sure this point is in both line segments
	if (x1 < x_prime < x2 or x2 < x_prime < x1) and (x3 < x_prime < x4 or x4 < x_prime < x3):
			return (x_prime, y_prime)

	return None
	
	# end of black magic - you may now touch

# --- test cases ---
'''
x1 = 0
y1 = 0
z1 = 0

x2 = 2
y2 = 2
z2 = 2

x3 = 2
y3 = 0
z3 = 0

x4 = 0
y4 = 2
z4 = 2

print(lineIntersect3D(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4))
'''