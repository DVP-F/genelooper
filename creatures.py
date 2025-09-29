# from __future__ import annotations
import random

class Creature:
	__slots__ = ["inheritance", "genes"]

	def __init__(self, genes: str = ""):
		self.inheritance = []
		self.genes = genes
		self.mutate()

	def mutate(self):
		...
