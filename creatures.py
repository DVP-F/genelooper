# from __future__ import annotations
import random

# noinspection PyTypeChecker
class Genes:
	stats = [
		"agr"	,	# Aggression
		"str"	,	# Strength
		"mut"	,   # Mutation
		"val"	,	# Value
		"sth"	]	# Stealth

	@staticmethod
	def _make_stats_dict(*, values: list[float,] = None):
		ret = {}
		for i in Genes.stats: # maps values to Genes.stats one-to-one
			ret += {Genes.stats[i]: 0.0 if values is None else float(abs(values[i])) if len(values) >= i-1 else 0.0,}
		return ret

	genevalues = {
		'<': # in principle equal to a chr() string - one character
			_make_stats_dict(),
		'>': 
			_make_stats_dict(),
		'@': 
			_make_stats_dict(),
		'#': 
			_make_stats_dict(),
		'¤': 
			_make_stats_dict(),
		'$': 
			_make_stats_dict(),
		'%': 
			_make_stats_dict(),
		'&': 
			_make_stats_dict(),
		'|': 
			_make_stats_dict(),
		'§':
			_make_stats_dict(values = [0.0, 0.0, 0.0, 0.0, 2.8]),
		'^':
			_make_stats_dict(values = [3.0, 6.1, 5.9, 11.6, 13.4]),
		'µ':
			_make_stats_dict(values = [5.8, 18.1, 8.2, 11.5, 7.3]),
		'ω':
			_make_stats_dict(values = [9.7, 12.3, 0.1, 20.0, 4.6]), # UωU
		'!':
			_make_stats_dict(values = [13.2, 14.7, 18.0, 9.4, 0.0])
		}


# noinspection PyTypeChecker
class Creature:
	__slots__ = ["inheritance", "genes", "stats"]

	@classmethod
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

	@classmethod
	def mutate(self):
		return

