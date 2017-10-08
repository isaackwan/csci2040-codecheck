from browser import document, alert, window
from unittest import TestCase, TextTestRunner, defaultTestLoader
import sys

class Lab3:
	class _P1Test(TestCase):
		def test_upper(self):
			self.assertEqual('foo'.upper(), 'FOO')

		def test_isupper(self):
			self.assertTrue('FOO'.isupper())
			self.assertFalse('Foo'.isupper())

	def __init__(self):
		super().__init__()

	def upload(self, name, content):
		exec(content)

	def finishedUpload(self):
		window.console.log('finished upload')
		suite = defaultTestLoader.loadTestsFromTestCase(Lab3._P1Test)
		TextTestRunner().run(suite)
		window.console.log('finished running test suite')

# setup stderr
def write(data):
    document['result'].innerText += str(data)

sys.stderr.write = write

lab3 = Lab3()

def handleUpload(event):
	lab3.upload(event.detail.name, event.detail.body)

def handleFinishedUpload(event):
	lab3.finishedUpload()

document['drop_zone'].bind('upload', handleUpload)
document['drop_zone'].bind('finishedUpload', handleFinishedUpload)
document['drop_zone'].innerText = 'Ready, please drop your Python3 (.py) files here'