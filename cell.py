import random

class Cell:
	def __init__(self):
		self.queens = []
		for i in range(8):
			self.queens += [int(random.uniform(0,8))]
		self.fitness = 0
		self.computeFitness()

	def computeFitness(self):
		self.fitness = 0
		for i in range(len(self.queens)):
			for j in range(i+1,len(self.queens)):
				if self.queens[i]==self.queens[j]:
					self.fitness += 2
					#print '[%d vs %d]' % (i,j)
					#print '(%d , %d) fit=%d' % (self.queens[i],self.queens[j],self.fitness)
				elif abs((self.queens[i]-self.queens[j])/float(i-j))==1:
					self.fitness += 2
					#print '[%d vs %d]' % (i,j)
					#print '(%d , %d) fit=%d' % (self.queens[i],self.queens[j],self.fitness)
	def setQueens(self,queens):
		self.queens = queens
