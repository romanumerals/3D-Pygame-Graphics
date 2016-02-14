import math

class Point:

	def __init__(self, x, y, z):

		self.x = x
		self.y = y
		self.z = z

	def dist(self, p2):
		dx = p2.x - self.x
		dy = p2.y - self.y
		dz = p2.z - self.z

		# simple distance formula
		return math.sqrt(dx**2 + dy**2 + dz**2)

	def positionVector(self):
		return AVector3(self.x, self.y, self.z)

	def vectorToPoint(self, p2):
		return AVector3(p2.x-self.x, p2.y-self.y, p2.z-self.z)

	def __str__(self):
		return "(" + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')' 

class Line:

	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

	def dist(self, p3):
		a = self.p1.vectorToPoint(p3)
		b = self.p1.vectorToPoint(self.p2)
		return a.crossWith(b).getMagnitude()/b.getMagnitude()

	def ifOnLine(self, p3):
		a = self.p1.vectorToPoint(p3)
		b = self.p1.vectorToPoint(self.p2)

		return not bool(a.angleBetween(b))

class TriangularPlane:

	def __init__(self, p1, p2, p3):
		self.p1 = p1
		self.p2 = p2
		self.p3 = p3
		self.e1 = Line(p1, p2)
		self.e2 = Line(p2, p3)
		self.e3 = Line(p1, p3)

# other shit
class VPlane:

	def __init__(self, v1, v2, p1):
		self.planeOrigin = p1
		self.planeX = v1
		self.planeY = v2

	def projectOntoPlaneVector(self, v1):
		# rounding reduced to two decimals for less strict definition of backwards
		if abs(v1.angleBetween(self.planeX)) > math.pi/2:
			x = -v1.projectOnto(self.planeX).getMagnitude()
		else:
			x = v1.projectOnto(self.planeX).getMagnitude()

		if abs(v1.angleBetween(self.planeY)) > math.pi/2:
			y = -v1.projectOnto(self.planeY).getMagnitude()
		else:
			y = v1.projectOnto(self.planeY).getMagnitude()


		return (x, y)

	def projectOntoPlanePoint(self, p1):
		QP = p1.positionVector().addNew(self.planeOrigin.positionVector().scalarMultiplyNew(-1))
		return self.projectOntoPlaneVector(QP)

	def projectOntoPlaneVPoint(self, p1):
		QP = p1.addNew(self.planeOrigin.positionVector().scalarMultiplyNew(-1))
		return self.projectOntoPlaneVector(QP)

	def rotateAboutX(self, theta):
		self.planeX.rotateAboutX(theta)
		self.planeY.rotateAboutX(theta)

	def rotateAboutY(self, theta):
		self.planeX.rotateAboutY(theta)
		self.planeY.rotateAboutY(theta)

	def rotateAboutZ(self, theta):
		self.planeX.rotateAboutZ(theta)
		self.planeY.rotateAboutZ(theta)

	def getNormal(self):
		return self.planeX.crossWith(self.planeY)

	def getConstant(self, normal):
		temp1 = normal.x * self.planeOrigin.x
		temp2 = normal.y * self.planeOrigin.y
		temp3 = normal.z * self.planeOrigin.z
		return temp1 + temp2 + temp3

	def getCollidePointWithVLine(self, l1):
		n = self.getNormal()
		temp1 = self.getConstant(n) - (n.x*l1.positionVector.x + n.y*l1.positionVector.y + n.z*l1.positionVector.z)
		temp2 = n.x*l1.directionVector.x + n.y*l1.directionVector.y + n.z*l1.directionVector.z
		k = temp1/temp2
		pnt = l1.getVPointAt(k)
		tmp = self.projectOntoPlaneVPoint(pnt)
		return tmp

	def translate(self, v1):
		self.planeOrigin = self.planeOrigin.positionVector().addNew(v1).getPoint()


class VLine:
	
	def __init__(self, v1, p1):
		self.directionVector = v1
		self.positionVector = p1.positionVector()

	def ifPointOnLine(self, p1):
		k1 =  ((p1.x-self.positionVector.x) / self.directionVector.x)
		k2 =  ((p1.y-self.positionVector.y) / self.directionVector.y)
		k3 =  ((p1.z-self.positionVector.z) / self.directionVector.z)

		return k1 == k2 == k3

	def getVPointAt(self, k):
		return self.positionVector.addNew(self.directionVector.scalarMultiplyNew(k))

	def __str__(self):
		return '(x, y, z) = ' + str(self.positionVector) + ' + k' + str(self.directionVector)

class AVector3:

	def __init__(self, x, y, z):
		self.x = round(x, 5)
		self.y = round(y, 5)
		self.z = round(z, 5)

	def add(self, v2):
		self.x += v2.x
		self.y += v2.y
		self.z += v2.z

	def addNew(self, v2):
		return AVector3(self.x+v2.x, self.y+v2.y, self.z+v2.z) 

	def scalarMultiply(self, s2):
		self.x *= s2
		self.y *= s2
		self.z *= s2

	def scalarMultiplyNew(self, s2):
		return AVector3(self.x*s2, self.y*s2, self.z*s2)

	def dotProduct(self, v2):
		p1 = self.x * v2.x
		p2 = self.y * v2.y
		p3 = self.z * v2.z
		return p1 + p2 + p3

	def crossWith(self, v2):
		x = self.y * v2.z - self.z * v2.y
		y = self.z * v2.x - self.x * v2.z
		z = self.x * v2.y - self.y * v2.x
		return AVector3(x, y, z)

	def getMagnitude(self):
		return math.sqrt(self.x**2 + self.y**2 + self.z**2)

	def getUnitVector(self):
		m = self.getMagnitude()
		return AVector3(round(self.x/m, 5), round(self.y/m, 5), round(self.z/m, 5))

	def angleBetween(self, v2):
		try:
			return math.acos(self.dotProduct(v2)/(self.getMagnitude() * v2.getMagnitude()))
		except:
			return 0

	def projectOnto(self, v2):
		# project self onto v2
		# look mate, it just fucking works
		# don't question it... don't
		return v2.scalarMultiplyNew(round(self.dotProduct(v2)/v2.dotProduct(v2), 5))

	def rotateAboutX(self, theta):
		tmp = self.getUnitVector()
		if not(self.y == 0 and self.z == 0):
			self.x = self.x
			self.y = round(math.sin(math.asin(tmp.y)-theta), 5)
			self.z = round(math.cos(math.acos(tmp.z)-theta), 5)

	def rotateAboutY(self, theta):
		tmp = self.getUnitVector()
		if not(self.x == 0 and self.z == 0):
			ang = math.atan2(self.z, self.x)-theta
			self.x = round(math.cos(ang), 5)
			self.y = self.y
			self.z = round(math.sin(ang), 5)

	def rotateAboutZ(self, theta):
		tmp = self.getUnitVector()
		if not(self.x == 0 and self.y == 0):
			self.x = round(math.sin(math.asin(tmp.x)-theta), 5)
			self.y = round(math.cos(math.acos(tmp.y)-theta), 5)
			self.z = self.z

	def getPoint(self):
		return Point(self.x, self.y, self.z)

	def __str__(self):
		return "{" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "}"