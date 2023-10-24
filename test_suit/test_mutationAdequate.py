"""test_mutationAdequate.py

Program to ensure that mutations are all killed before reaching
the end of the program."""
import unittest
import mutpy
from enum import Enum
from isTriangle import Triangle


class TestMutants(unittest.TestCase):
    """Unit test class for testing mutants."""

    def test_scalene(self):
        """Test that the mutant is killed upon
        a^2+b^2=c^2."""
        self.assertEqual(Triangle.classify(26, 14, 15), Triangle.Type.SCALENE)

    def test_invalid_lengths(self):
        self.assertEqual(Triangle.classify(1, 3, 5), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 5, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(3, 1, 5), Triangle.Type.INVALID)

    def test_equilateral(self):
        self.assertEqual(Triangle.classify(3, 3, 3), Triangle.Type.EQUILATERAL)

    def test_isoceles(self):
        """Test that the mutant is killed upon
        a==b."""
        self.assertEqual(Triangle.classify(2, 2, 3), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(3, 2, 2), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(3, 2, 3), Triangle.Type.ISOSCELES)


if __name__ == "__main__":
    unittest.main()
