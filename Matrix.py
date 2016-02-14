class Matrix3:

	def __init__(self, r1, r2, r3, augment):
		self.matrix = [r1, r2, r3]
		self.augment

	def scalarMultiplyRow(self, scalar, row):
		for i in range(3):
			self.matrix[row][i] *= scalar
		self.augment[row] *= scalar

	def scalarDivideRow(self, scalar, row):
		for i in range(3):
			self.matrix[row][i] /= scalar
		self.augment[row] /= scalar

	def addRowToOther(self, r1, r2):
		for i in range(3):
			self.matrix[r2] += self.matrix[r1]
		self.augment[r2] += self.augment[r1]

	def solveYZ(self):
		# will begin row-reduction algorithm

		for i in range(1, 3):
			self.scalarDivideRow(self.matrix[i][0], i)
			self.scalarMultiplyRow(self.matrix[0][0], i)
			self.scalarMultiplyRow(-1, i)
			self.addRowToOther(0, i)

		self.scalarDivideRow(self.matrix[2][1], 2)
		self.scalarMultiplyRow(self.matrix[1][1], 2)
		self.scalarMultiplyRow(-1, 2)
		self.addRowToOther(1, 2)

		self.scalarDivideRow(self.matrix[1][1], 1)
		self.scalarDivideRow(self.matrix[2][2], 2)

		y = self.augment[1] - self.matrix[1][2]*self.augment[2]
		z = self.augment[2]

		return (y, z)

		




