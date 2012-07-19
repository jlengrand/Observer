#!/usr/bin/env python

import Observer

class Observable():
	"""
	"""

	def __init__(self):
		"""
		"""
		self.val = 1
		self.obs_collection = []


	def subscribe(self, observer):
		"""
		"""
		try:
			if not(observer in self.obs_collection):
				self.obs_collection.append(observer)
				print "%s added to collection" %(str(observer))
			else:
				print "%s already in collection" %(str(observer))

		except TypeError:
			print "Failed to add %s" %(str(observer))

	def unsubscribe(self, observer):
		"""
		"""
		try:
			if observer in self.obs_collection:
				self.obs_collection.remove(observer)
				print "%s removed from collection" %(str(observer))
			else:
				print "%s not in collection" %(str(observer))

		except TypeError:
			print "Failed to remove %s" %(str(observer))

	def notify(self, message):
		"""
		"""
		for observer in self.obs_collection:
			print "sent %s to %s" %(message, str(observer))
			observer.update(message)


	def set_val(self, val=1):
		"""
		"""
		self.val += val
		self.notify(str(self.val))
