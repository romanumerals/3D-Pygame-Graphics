import Geometry
import ShapeLibrary as SL
import math
import pygame
pygame.init()

# constants

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class UI:

	def __init__(self):
		self.running = True
		self.screen = pygame.display.set_mode((600, 480))
		self.objects = [SL.Cube(0, 0, 0, 100), SL.Cube(100, 0, 0, 50)]
		canvas = Geometry.VPlane(Geometry.AVector3(1, 0, 1), Geometry.AVector3(0, 1, 0), Geometry.Point(0, 0, 0))
		self.cam = Camera(canvas, 150, 480, 600, self.objects)
		self.delay = 0

	def runningLoop(self):

		mb = pygame.mouse.get_pressed()
		k = pygame.key.get_pressed()

		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				self.running = False

		if self.delay == 0:
			if mb[0] == 1:
				self.cam.screen.rotateAboutY(0.01)
				self.delay = 1
			if mb[2] == 1:
				self.cam.screen.rotateAboutY(-0.01)
				self.delay = 1
			if k[pygame.K_w]:
				self.cam.screen.translate(Geometry.AVector3(1, 0, 0))
				self.delay = 1
			if k[pygame.K_s]:
				self.cam.screen.translate(Geometry.AVector3(-1, 0, 0))
				self.delay = 1
			if k[pygame.K_a]:
				self.cam.screen.translate(Geometry.AVector3(0, 0, 1))
				self.delay = 1
			if k[pygame.K_d]:
				self.cam.screen.translate(Geometry.AVector3(0, 0, -1))
				self.delay = 1
		if self.delay > 0:
			self.delay -= 1

		self.cam.draw()
		self.screen.blit(self.cam.canvas, (0, 0))
		pygame.display.flip()

	def run(self):
		while self.running:
			self.runningLoop()

class Camera:

	def __init__(self, canvas, distance, heightres, widthres, pointed_at):
		# self.location = Geometry.Point(x, y, z)

		self.screen = canvas
		self.distance = distance

		self.resolution = (widthres, heightres)

		self.objects = pointed_at
		self.canvas = pygame.Surface(self.resolution)

	def draw(self):
		self.canvas.fill(BLACK)

		view = self.screen.getNormal().getUnitVector().scalarMultiplyNew(self.distance).getPoint()

		for i in self.objects:
			line_to_center = Geometry.VLine(view.vectorToPoint(i.center), i.center)
			c = self.screen.getCollidePointWithVLine(line_to_center)
			c = (int(c[0]) + 300, int(c[1]) + 240)
			pygame.draw.circle(self.canvas, RED, c, 2)
			for e in i.edge:
				line_to_p1 = Geometry.VLine(view.vectorToPoint(i.verteces[e[0]]), i.verteces[e[0]])
				line_to_p2 = Geometry.VLine(view.vectorToPoint(i.verteces[e[1]]), i.verteces[e[1]])
				p1 = self.screen.getCollidePointWithVLine(line_to_p1)
				p2 = self.screen.getCollidePointWithVLine(line_to_p2)
				p1 = (p1[0] + 300, p1[1] + 240)
				p2 = (p2[0] + 300, p2[1] + 240)
				pygame.draw.line(self.canvas, GREEN, p1, p2)

UI().run()