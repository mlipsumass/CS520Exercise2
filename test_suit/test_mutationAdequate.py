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
        # try:
        #     self.assertEqual(Triangle.classify(5, 10, 15), Triangle.Type.SCALENE)
        # except AssertionError as exc:
        #     return
        self.assertEqual(Triangle.classify(24, 10, 15), Triangle.Type.SCALENE)

    # def test_equilateral(self):
    #     """Test that the mutant is killed upon
    #     a==b==c."""
    #     self.assertEqual(Triangle.classify(1, 1, 1), Triangle.Type.EQUILATERAL)

    # def test_isoceles(self):
    #     """Test that the mutant is killed upon
    #     a==b."""
    #     self.assertEqual(Triangle.classify(2, 2, 3), Triangle.Type.ISOSCELES)
    #     self.assertEqual(Triangle.classify(3, 2, 2), Triangle.Type.ISOSCELES)
    #     self.assertEqual(Triangle.classify(3, 2, 3), Triangle.Type.ISOSCELES)


if __name__ == "__main__":
    unittest.main()
