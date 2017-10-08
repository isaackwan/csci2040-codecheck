from browser import document
from unittest import TestCase, TextTestRunner, defaultTestLoader
import sys

class Lab3():
	class _P1Test(TestCase):
		def test_box_constructor_works(self):
			pass

		def test_lt_method(self):
			self.assertTrue(3 < 2)

	def upload(self, name, content):
		exec(content)

	def finishedUpload(self):
		print('finished upload')
		suite = defaultTestLoader.loadTestsFromTestCase(Lab3._P1Test)
		TextTestRunner().run(suite)
		print('finished running test suite')

# setup stderr
def write(data):
    document['result'].innerText += str(data)

sys.stderr.write = write

lab3 = Lab3()

def handleUpload(event):
	lab3.upload(event.detail.name, event.detail.body)

def handleFinishedUpload(event):
	lab3.finishedUpload()
	document['drop_zone'].innerText = 'Retry? Please refresh this page before proceeding'

document['drop_zone'].bind('upload', handleUpload)
document['drop_zone'].bind('finishedUpload', handleFinishedUpload)
document['drop_zone'].innerText = 'Ready, please drop your Python3 (.py) files here'