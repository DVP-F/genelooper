from __future__ import annotations
import random

# noinspection PyTypeChecker
class Creature:
	__slots__ = ["current_string", "lineage", "genes", "bias"]

	def __init__(self, *, genes: dict|list[dict] = {'mutation_rate':1, 'aggression':1, 'symmetry':2, }, bias: int = 0, lineage: list[dict] = []):
		self.current_string = ""
		self.lineage = lineage
		if type(genes) == dict:
			self.genes = genes
		elif genes is None: self.genes = {'mutation_rate': random.randint(1, 20), 'aggression': random.randint(1, 8), 'symmetry': random.randint(1, 5), }
		elif type(genes) == list[dict]: self.genes = []; self.cross_genes(genes)
		self.bias = bias
		self.mutate()

	def mutate(self):
		for i in self.genes:
			for _ in range(0, max(1, self.genes['mutation_rate']), 107):
				self.genes[i] += random.choice([random.randint(0, 5), random.randint(-5, 0)])
			for _ in range(0, max(1, self.genes['mutation_rate']), int(500-1000//max(1, abs(self.bias)))):
				self.genes[i] += self.bias//30
		self.genes['mutation_rate'] = max(5, min(self.genes['mutation_rate'], 1000))
		self.genes['aggression'] = max(1, min(self.genes['aggression'], 100))
		self.genes['symmetry'] = max(0, min(self.genes['symmetry'], 20))
		self.lineage += (self.genes,)

	def cross_genes(self, genes: list[dict]):
		self.genes = {'mutation_rate': random.choice([genes[0][0], genes[1][0]]), 'aggression': random.choice([genes[0][1], genes[1][1]]),
					'symmetry': random.choice([genes[0][2], genes[1][2]])}
		self.lineage += (self.genes,)

