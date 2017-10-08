from unittest import TestCase, TextTestRunner, TestSuite, defaultTestLoader
from .labcheck import LabCheck

class P1Test(TestCase):
	def test_empty_list(self):
		self.assertEqual(unique([]), [])

	def test_unique_list(self):
		self.assertEqual(unique(['a', 'b', 'c', '72', 72, 'amazing']), ['a', 'b', 'c', '72', 72, 'amazing'])

	def test_non_unique_list(self):
		self.assertEqual(unique(['a', 'b', 'a', 'b', 'b', 'c', 'c']), ['a', 'b', 'c'])

class P2Test(TestCase):
	def test_lt(self):
		box1 = Box(1)
		box2 = Box(2)
		self.assertTrue(box1 < box2)

	def test_le(self):
		box1 = Box(1)
		box2 = Box(2)
		box3 = Box(2)
		self.assertTrue(box1 <= box2)
		self.assertTrue(box3 <= box2)

	def test_gt(self):
		box1 = Box(1)
		box2 = Box(2)
		self.assertTrue(box2 > box1)

	def test_ge(self):
		box1 = Box(1)
		box2 = Box(2)
		box3 = Box(2)
		self.assertTrue(box2 >= box1)
		self.assertTrue(box2 >= box3)

	def test_eq(self):
		box1 = Box(2)
		box2 = Box(2)
		self.assertTrue(box2 == box1)

	def test_ne(self):
		box1 = Box(1)
		box2 = Box(2)
		self.assertTrue(box2 != box1)

	def test_mul(self):
		box1 = Box(3)
		box2 = Box(2)
		self.assertEquals(Box(6), box2 * box1)

class Lab3(LabCheck):
	def finishedUpload(self):
		suite = TestSuite()
		suite.addTests(defaultTestLoader.loadTestsFromTestCase(P1Test))
		suite.addTests(defaultTestLoader.loadTestsFromTestCase(P2Test))
		TextTestRunner().run(suite)

	def upload(self, name, body):
		if name[-2:] != 'py':
			raise Exception('Please upload only Python (.py) files!')

		exec(body, globals(), globals())