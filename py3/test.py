from unittest import TestCase, TextTestRunner, defaultTestLoader


class Lab3Test(TestCase):
	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')
		self.assertEqual('foo'.upper(), 'FO2O')

	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

suite = defaultTestLoader.loadTestsFromTestCase(Lab3Test)
TextTestRunner().run(suite)