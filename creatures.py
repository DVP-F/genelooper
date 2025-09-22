from __future__ import annotations
import random

class Creature:
	__slots__ = ["current_string", "iterations", "genes"]

	def __init__(self, genes: dict = {'mutation_rate':0.1, 'aggression':1.0, 'symmetry':2.0, }):
		self.current_string = ""
		self.iterations = []
		self.genes = genes
		self.mutate()

	def mutate(self):
		for i in self.genes:
			for _ in range(max(1, int(self.genes['mutation_rate']))):
				self.genes[i] += random.choice([random.uniform(0.0, 0.5), random.uniform(-0.5, 0.0)])
		self.genes['mutation_rate'] = max(0.05, min(self.genes['mutation_rate'], 10.0))
		self.genes['aggression'] = max(1.0, min(self.genes['aggression'], 10.0))
		self.genes['symmetry'] = max(0.0, min(self.genes['symmetry'], 5.0))
