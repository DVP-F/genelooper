# from __future__ import annotations
import random

# noinspection PyTypeChecker
class Genes:
	stats = [
		"agr"	,
		"str"	,
		"mut"	,
		"val"	,
		"sth"	]

	genevalues = {
		'<': { # in principle equal to a chr() string - one character
			"agr": 0.0,	# Aggression 
			"str": 0.0,	# Strength 
			"mut": 0.0, # Mutation 
			"val": 0.0,	# Value 
			"sth": 0.0	# Stealth 
		},
		'>': {
			"agr": 0.0,
			"str": 0.0,
			"mut": 0.0,
			"val": 0.0,
			"sth": 0.0
		},
		'@': {
			"agr": 0.0,
			"str": 0.0,
			"mut": 0.0,
			"val": 0.0,
			"sth": 0.0
		},
		'#': {
			"agr": 0.0,
			"str": 0.0,
			"mut": 0.0,
			"val": 0.0,
			"sth": 0.0
		},
		'¤': {
			"agr": 0.0,
			"str": 0.0,
			"mut": 0.0,
			"val": 0.0,
			"sth": 0.0
		},
		'$': {
			"agr": 0.0,
			"str": 0.0,
			"mut": 0.0,
			"val": 0.0,
			"sth": 0.0
		},
		'%': {
			"agr": 0.0,
			"str": 0.0,
			"mut": 0.0,
			"val": 0.0,
			"sth": 0.0
		},
		'&': {
			"agr": 0.0,
			"str": 0.0,
			"mut": 0.0,
			"val": 0.0,
			"sth": 0.0
		},
		'|': {
			"agr": 0.0,
			"str": 0.0,
			"mut": 0.0,
			"val": 0.0,
			"sth": 0.0
		},
		'§': {
			"agr": 0.0,
			"str": 0.0,
			"mut": 0.0,
			"val": 0.0,
			"sth": 2.8
		},
		'^': {
			"agr": 3.0,
			"str": 6.1,
			"mut": 5.9,
			"val": 11.6,
			"sth": 13.4
		},
		'µ': {
			"agr": 5.8,
			"str": 18.1,
			"mut": 8.2,
			"val": 11.5,
			"sth": 7.3
		},
		'ω': { # UωU 
			"agr": 9.7,
			"str": 12.3,
			"mut": 0.1,
			"val": 20.0,
			"sth": 4.6
		},
		'!': {
			"agr": 13.2,
			"str": 14.7,
			"mut": 18.0,
			"val": 9.4,
			"sth": 0.0
		},
		}

	@staticmethod
	def _make_stats_dict(*, values: list[float,] = None):
		ret = {}
		for i in Genes.stats:
			ret += {Genes.stats[i]: 0.0 if values == None else values[i],}
		return ret


# noinspection PyTypeChecker
class Creature:
	__slots__ = ["inheritance", "genes", "stats"]

	def __init__(self, genes: str = ""):
		self.inheritance = []
		self.genes = genes
		# self.mutate()
		self.stats = {}
		for i in Genes.stats:
			self.stats += {Genes.stats[i]: 0.0,} # dynamic stat dict generation
		for i in range(len(self.genes)):
			for j in Genes.stats:
			# actually just sums up every effect of every gene - but its dynamic and way shorter to write. might cover the calculation tree in doc
				self.stats[j] += Genes.genevalues[self.genes[i]][j]
		self.stats["mut"] / len(self.genes) # average out
		for i in self.stats: #? round off to one decimal place
			c = int((self.stats[i] % 1) * 10) / 10
			self.stats[i] = (self.stats[i] // 1) + c

	def mutate(self):
		return

