import cell
import random

class Population:
	def __init__(self,size,maxIt,repRate,mutRate):
		"""
			size: number of cells in the population
			maxIt: number of maximum iterations (-1 to set it as infinity)
			repRate: fraction of population to be renewed
			mutRate: value defining probability of mutation during reproduction
		"""
		self.size = size
		self.maxIt = maxIt
		self.repRate = repRate
		self.mutRate = mutRate
		self.pop = []
		for i in range(self.size):
			self.pop += [cell.Cell()]
		self.sort()
	def sort(self):
		self.pop = self.quicksort(self.pop)
	def quicksort(self,list):
		if len(list)<=1:
			return list
		else:
 			left = [cel for cel in list[1:] if cel.fitness<list[0].fitness]
			right = [cel for cel in list[1:] if cel.fitness>=list[0].fitness]
			return self.quicksort(left)+[list[0]]+self.quicksort(right)
	def printPop(self):
		for cel in self.pop:
			print cel.queens + ['; '] +[cel.fitness]
	def reproduce(self,cellA,cellB):
		queens = []
		for i in range(8):
			if random.random()<self.mutRate:
				queens += [int(random.uniform(0,8))]
			else:
				if random.random()<0.5:
					queens += [cellA.queens[i]]
				else:
					queens += [cellB.queens[i]]
		cellN = cell.Cell()
		cellN.setQueens(queens)
		cellN.computeFitness()
		return cellN
	def repCycle(self):
		cutIdx = int(self.size*self.repRate)
		newPop = self.pop[:(self.size-cutIdx)]
		prob = []
		sumInv = 0
		for cell in self.pop:
			sumInv += 1/(cell.fitness+0.1)
		for i in range(self.size):
			sum = 0
			for j in range(i):
				sum += prob[j]
			prob += [sum+((1/(self.pop[i].fitness+0.1))/sumInv)]
		for i in range(cutIdx):
			cellA = self.pop[self.selectCell(prob)]
			cellB = self.pop[self.selectCell(prob)]
			newPop += [self.reproduce(cellA,cellB)]
		self.pop = newPop
	def selectCell(self,probList):
		rndm = random.random()
		for i in range(len(probList)):
			if rndm<=probList[i]:
				return i
		return len(probList)
	def iterate(self):
		self.sort()
		iteration = 0
		if self.maxIt==-1:
			while self.pop[0].fitness!=0:
				self.repCycle()
				self.sort()
				iteration += 1
				if iteration % 10 == 0 or self.pop[0].fitness==0:
					print [iteration]+[': ']+[self.pop[0].queens]+[';']+[self.pop[0].fitness]
		else:
			for i in range(self.maxIt):
				self.repCycle()
				self.sort()
				iteration += 1
				if iteration %10 == 0 or self.pop[0].fitness==0:
					print [iteration]+[': ']+[self.pop[0].queens]+[';']+[self.pop[0].fitness]
					if self.pop[0].fitness==0:
						break
