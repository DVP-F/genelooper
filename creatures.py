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
		for i in Genes.stats: # maps values and Genes.stats one-to-one
			ret += {Genes.stats[i]: 0.0 if values is None else float(abs(values[i])) if len(values) >= i-1 else 0.0,}
		return ret

	genes = ['<', '>', '@', '#', '¤', '$', '%', '&', '|', '§', '^', 'µ', 'ω', '!']

	genevalues = {
		genes[0]: # in principle equal to a chr() string - one character
			_make_stats_dict(values = [2.9, 7.3, 14.3, 5.2, 14.2]), # by convention  0.0 <= x <= 20.0
		genes[1]:
			_make_stats_dict(values = [18.2, 15.5, 17.9, 4.4, 15.0]),
		genes[2]:
			_make_stats_dict(values = [3.6, 9.1, 2.4, 5.0, 13.8]),
		genes[3]:
			_make_stats_dict(values = [9.8, 8.5, 7.8, 11.2, 4.2]),
		genes[4]:
			_make_stats_dict(values = [13.4, 2.3, 15.8, 18.3, 17.2]),
		genes[5]:
			_make_stats_dict(values = [9.1, 3.8, 6.1, random.uniform(4.0, 12.0), 2.6]), #? do you get it? because currency is inherent fallible and changes value wildly unpredictably and this is political comment with very socialist anarchist intents? why are you still reading this are you waiting for me to do? like *fuckgin kisses you sloppily* you like that huh? youre a naughty one huh? are you gonna be good for me? the answer is YES, puppy. >:3c
		genes[6]:
			_make_stats_dict(values = [11.0, 12.8, 11.5, 19.4, 9.3]),
		genes[7]:
			_make_stats_dict(values = [2.2, 18.2, 7.6, 10.5, 7.3]),
		genes[8]:
			_make_stats_dict(values = [16.8, 11.0, 4.5, 9.1, 3.9]),
		genes[9]:
			_make_stats_dict(values = [6.4, 9.7, 8.1, 8.2, 2.8]),
		genes[10]:
			_make_stats_dict(values = [3.0, 6.1, 5.9, 11.6, 13.4]),
		genes[11]:
			_make_stats_dict(values = [5.8, 18.1, 8.2, 11.5, 7.3]),
		genes[12]:
			_make_stats_dict(values = [9.7, 12.3, 0.1, 20.0, 15.6]), # UωU
		genes[13]:
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
				# still a bit gross tho. has four getitem and a setitem like its effectively;
				# self.stats.__setitem__(j,(self.stats.__getitem__(j)+Genes.genevalues.__getitem__(self.genes.__getitem__(i))).__getitem__(j))
		self.stats["mut"] / len(self.genes) # average out
		for i in self.stats: #? round off to one decimal place
			c = int((self.stats[i] % 1) * 10) / 10
			self.stats[i] = (self.stats[i] // 1) + c

	@classmethod
	def mutate(self):
		for i in range(len(self.genes)):
			for j in range(len(Genes.stats)):
				if random.uniform(0.0, 20.0) < Genes.genevalues[self.genes[i]][j]:
					temp = self.genes[0:i:1] #? hope to find a way around this but for now its necessary to slice
					self.genes = self.genes[i:-1:1]
					self.genes.replace(self.genes[i], random.choice(Genes.genes), 1)
					self.genes = temp + self.genes

