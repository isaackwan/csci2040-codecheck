from browser import document, alert, window
from unittest import TestCase, main

class Lab3Test(TestCase):
	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')
		self.assertEqual('foo'.upper(), 'FO2O')

	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

class Lab3:
	def __init__(self):
		super().__init__()

	def upload(self, name, content):
		exec(content)

	def finishedUpload(self):
		alert('finished upload')
		result = Lab3Test()
		window.console.log(result)
		main()
		print(result)
		alert('run')

lab3 = Lab3()

def handleUpload(event):
	lab3.upload(event.detail.name, event.detail.body)

def handleFinishedUpload(event):
	lab3.finishedUpload()

document['drop_zone'].bind('upload', handleUpload)
document['drop_zone'].bind('finishedUpload', handleFinishedUpload)