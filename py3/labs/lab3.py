from unittest import TestCase, TextTestRunner, defaultTestLoader

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

