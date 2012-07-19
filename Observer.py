#!/usr/bin/env python

class Observer():
	"""
	"""

	def __init__(self, name="bob"):
		"""
		"""
		self.name = name


	def update(self, message):
		"""
		"""
		if message is not None:
			print "%s received %s" %(self.name, message)

	def __str__(self):
		return self.name