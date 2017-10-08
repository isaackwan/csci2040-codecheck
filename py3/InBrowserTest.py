from abc import ABCMeta

class InBrowserTest(metaclass=ABCMeta):
	"""
	BrowserTest is the interface for each testing class. Usually one "lab" have two testing classes, one for Python 2 & one for Python 3.

	For performance reasons, however, implementations of this interface will not inherit this class directly.
	"""
	def __init__(self):
		pass

	def upload(self, name, content):
		pass

	def finishedUpload(self):
		pass

	