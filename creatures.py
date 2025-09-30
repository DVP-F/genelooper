# from __future__ import annotations
import random

# noinspection PyTypeChecker
class Genes:
	genevalues = {
		'<': { # in principle equal to a chr() string - one character
			"agr": 0.0,	# Aggression 
			"str": 0.0,	# Strength 
			"mut": 0.0, # Mutation 
			"val": 0.0,	# Value 
			"sth": 0.0	# Stealth 
		},
		'>': {
			"agr": 0.0,	# Aggression 
			"str": 0.0,	# Strength 
			"mut": 0.0, # Mutation 
			"val": 0.0,	# Value 
			"sth": 0.0	# Stealth 
		},
		'@': {
			"agr": 0.0,	# Aggression 
			"str": 0.0,	# Strength 
			"mut": 0.0, # Mutation 
			"val": 0.0,	# Value 
			"sth": 0.0	# Stealth 
		},
		'#': {
			"agr": 0.0,	# Aggression 
			"str": 0.0,	# Strength 
			"mut": 0.0, # Mutation 
			"val": 0.0,	# Value 
			"sth": 0.0	# Stealth 
		},
		'¤': {
			"agr": 0.0,	# Aggression 
			"str": 0.0,	# Strength 
			"mut": 0.0, # Mutation 
			"val": 0.0,	# Value 
			"sth": 0.0	# Stealth 
		},
		'$': {
			"agr": 0.0,	# Aggression 
			"str": 0.0,	# Strength 
			"mut": 0.0, # Mutation 
			"val": 0.0,	# Value 
			"sth": 0.0	# Stealth 
		},
		'%': {
			"agr": 0.0,	# Aggression 
			"str": 0.0,	# Strength 
			"mut": 0.0, # Mutation 
			"val": 0.0,	# Value 
			"sth": 0.0	# Stealth 
		},
		'&': {
			"agr": 0.0,	# Aggression 
			"str": 0.0,	# Strength 
			"mut": 0.0, # Mutation 
			"val": 0.0,	# Value 
			"sth": 0.0	# Stealth 
		},
		'|': {
			"agr": 0.0,	# Aggression 
			"str": 0.0,	# Strength 
			"mut": 0.0, # Mutation 
			"val": 0.0,	# Value 
			"sth": 0.0	# Stealth 
		},
		'§': {
			"agr": 0.0,	# Aggression 
			"str": 0.0,	# Strength 
			"mut": 0.0, # Mutation 
			"val": 0.0,	# Value 
			"sth": 2.8	# Stealth 
		},
		'^': {
			"agr": 3.0,	# Aggression 
			"str": 6.1,	# Strength 
			"mut": 5.9, # Mutation 
			"val": 11.6,# Value 
			"sth": 13.4	# Stealth 
		},
		'µ': {
			"agr": 5.8,	# Aggression 
			"str": 18.1,# Strength 
			"mut": 8.2, # Mutation 
			"val": 11.5,# Value 
			"sth": 7.3	# Stealth 
		},
		'ω': { # UωU 
			"agr": 9.7,	# Aggression 
			"str": 12.3,# Strength 
			"mut": 0.1, # Mutation 
			"val": 20.0,# Value 
			"sth": 4.6	# Stealth 
		},
		'!': {
			"agr": 13.2,# Aggression 
			"str": 14.7,# Strength 
			"mut": 18.0,# Mutation 
			"val": 9.4,	# Value 
			"sth": 0.0	# Stealth 
		},
		}


# noinspection PyTypeChecker
class Creature:
	__slots__ = ["inheritance", "genes", ""]

	def __init__(self, genes: str = ""):
		self.inheritance = []
		self.genes = genes
		self.mutate()

	def mutate(self):
		return
