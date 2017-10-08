from abc import ABCMeta

class Lab(metaclass=ABCMeta):
	"""
	Lab is the interface for each testing class.

	For performance reasons, however, implementations of this interface will not inherit this class directly.
	"""
	def __init__(self):
		pass

	def upload(self, name, content):
		pass

	def finishedUpload(self):
		pass

	