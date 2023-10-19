import unittest
from isTriangle import Triangle

class TriangleTest(unittest.TestCase):
	def test_negative_length(self):
		actual = Triangle.classify(1, -5, 2)
		expected = Triangle.Type.INVALID
		self.assertTrue(expected == actual)
        
	def test_invalid_lengths(self):
		actual = Triangle.classify(1, 3, 5)
		expected = Triangle.Type.INVALID
		self.assertTrue(expected == actual)
        
	def test_scalene(self):
		actual = Triangle.classify(2, 3, 4)
		expected = Triangle.Type.SCALENE
		self.assertTrue(expected == actual)

	def test_ab_isosceles(self):
		actual = Triangle.classify(2, 2, 3)
		expected = Triangle.Type.ISOSCELES
		self.assertTrue(expected == actual)

	def test_ac_isosceles(self):
		actual = Triangle.classify(2, 3, 2)
		expected = Triangle.Type.ISOSCELES
		self.assertTrue(expected == actual)

	def test_bc_isosceles(self):
		actual = Triangle.classify(3, 2, 2)
		expected = Triangle.Type.ISOSCELES
		self.assertTrue(expected == actual)

	def test_invalid_isosceles(self):
		actual = Triangle.classify(2, 2, 5)
		expected = Triangle.Type.INVALID
		self.assertTrue(expected == actual)

if __name__ == '__main__':
    unittest.main()
