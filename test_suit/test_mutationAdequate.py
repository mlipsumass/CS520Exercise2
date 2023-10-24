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
        val = Triangle.classify(26, 14, 15)
        self.assertEqual(Triangle.classify(26, 14, 15), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(15, 26, 14), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(14, 15, 26), Triangle.Type.SCALENE)

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

    def test_invalid_isoceles(self):
        self.assertEqual(Triangle.classify(6, 3, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(7, 3, 4), Triangle.Type.INVALID)

    def test_a_and_c_equal_to_b_invalid(self):
        self.assertEqual(Triangle.classify(3, 6, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(4, 7, 3), Triangle.Type.INVALID)

    def test_a_and_b_equal_to_c_invalid(self):
        self.assertEqual(Triangle.classify(3, 3, 6), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(4, 3, 7), Triangle.Type.INVALID)

    def test_b_and_c_equal_to_a_invalid(self):
        self.assertEqual(Triangle.classify(6, 3, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(7, 3, 4), Triangle.Type.INVALID)

    def test_put_negative_numbers(self):
        self.assertEqual(Triangle.classify(-1, -1, -1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(-1, 1, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, -1, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 1, -1), Triangle.Type.INVALID)

    def try_bunch_of_zeros(self):
        for i in range(-1, 1):
            for j in range(-1, 1):
                for k in range(-1, 1):
                    self.assertEqual(Triangle.classify(i, j, k), Triangle.Type.INVALID)


if __name__ == "__main__":
    unittest.main()
