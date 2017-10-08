from abc import ABCMeta, abstractmethod

class LabCheck(metaclass=ABCMeta):
	def __init__(self):
		pass

	@abstractmethod
	def upload(self, name, body):
		pass

	@abstractmethod
	def finishedUpload(self):
		pass

	