from pygame import *
from math import *

# --- constants ---
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

# --- functions ---

def hypot(dx, dy):
	return sqrt(dx**2 +dy**2)

# --- classes ---

class Camera:
        def __init__(self, x, y, z, ah, sw, sh):
		# x, y, and z are the position of the camera
		# ah is the agle it sees around itself
		# sw and sh are the shot width and the shot height in degrees - these determine the aspect ratio of the final image
                self.x = x
                self.y = y
                self.z = z
                self.ang_horizontal = ah

                self.screen_width = sw
                self.screen_height = sh

        def getImage(self, width, height, objects):
		# virt refers to a virtual "image"taken by the camera
                virt_image = Surface((width, height))
                virt_image.fill(black)
                for i in objects:
                        ang = degrees(atan2(i.center.y - self.y, i.center.x - self.x))
                        if True:
				# if the object is in the screen range
                                for e in i.edge:

                                        p1 = i.verteces[e[0]]
					# finds one point's shadow on the canvas
                                        dist = sqrt((p1.x - self.x)**2 + (p1.y - self.y)**2 + (p1.z - self.z)**2)
                                        dep = degrees(asin((p1.y - self.y) / dist))								# depression
                                        hor_ang = degrees(atan2(p1.z-self.z, p1.x-self.x))-self.ang_horizontal
                                        hor_off = ((width/2) * hor_ang)/(self.screen_width/2)
                                        ver_off = ((height/2) * dep)/(self.screen_height/2)
					# using ratios to determine the offset

                                        point1 = (width // 2 + hor_off, height // 2 - ver_off)
					

                                        p2 = i.verteces[e[1]]
					# now the other one
                                        dist = sqrt((p2.x - self.x)**2 + (p2.y - self.y)**2 + (p2.z - self.z)**2)
                                        dep = degrees(asin((p2.y - self.y) / dist))								# depression
                                        hor_ang = degrees(atan2(p2.z-self.z, p2.x-self.x))-self.ang_horizontal
                                        hor_off = ((width/2) * hor_ang)/(self.screen_width/2)
                                        ver_off = ((height/2) * dep)/(self.screen_height/2)

                                        point2 = (width // 2 + hor_off, height // 2 - ver_off)

                                        # now we connect the two

                                        draw.line(virt_image, green, point1, point2)
                return virt_image

        def rotate(self, ang):
                angle = self.ang_horizontal
                if ang > 0:
                        self.ang_horizontal = angle + ang
                        if self.ang_horizontal > 360:
                                self.ang_horizontal -= 360
                elif ang < 0:
                        self.ang_horizontal = angle + ang
                        if self.ang_horizontal < 0:
                                self.ang_horizontal += 360

class World:
        def __init__(self):
                points = [Point(5, -1, 4),Point(4, -1, 6), Point(3, -1, 5), Point(4, 1, 5)]
                self.objects = [Cube(0, 0, 0, 2), TriangleBasedPyramid(points)]

        def update(self):
                for i in objects:
                        i.update()

        def draw(self, camera):
                return camera.getImage(600, 480, self.objects)

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

# --- main ---

def main():
	world = World()
	camera = Camera(-5, 0, 2, 0, 45, 36)
	screen = display.set_mode((600, 480))
	running = True

	delay = 0

	while running:
		mb = mouse.get_pressed()
		k = key.get_pressed()

		for e in event.get():
			if e.type == QUIT:
				running = False

		if delay == 0:
			if mb[0] == 1:
				camera.rotate(1)
				delay = 10
			if mb[2] == 1:
				camera.rotate(-1)
				delay = 10
			if k[K_w]:
				camera.x += cos(radians(camera.ang_horizontal))
				camera.z += sin(radians(camera.ang_horizontal))
				delay = 10
			if k[K_s]:
				camera.x += cos(radians(camera.ang_horizontal-180))
				camera.z += sin(radians(camera.ang_horizontal-180))
				delay = 10
			if k[K_d]:
				camera.x += cos(radians(camera.ang_horizontal-90))
				camera.z += sin(radians(camera.ang_horizontal-90))
				delay = 40
			if k[K_a]:
				camera.x += cos(radians(camera.ang_horizontal+90))
				camera.z += sin(radians(camera.ang_horizontal+90))
				delay = 40

		if delay > 0:
			delay -= 1

		screen.blit(world.draw(camera), (0, 0))
		display.flip()

main()
quit()
