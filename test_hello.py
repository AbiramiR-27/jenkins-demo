import unittest
from hello import calculate_grade, calculate_average


class TestGradeCalculator(unittest.TestCase):

    def test_grade_A(self):
        self.assertEqual(calculate_grade(100), "A")
        self.assertEqual(calculate_grade(90), "A")
        self.assertEqual(calculate_grade(95.5), "A")

    def test_grade_B(self):
        self.assertEqual(calculate_grade(89.9), "B")
        self.assertEqual(calculate_grade(80), "B")

    def test_grade_C(self):
        self.assertEqual(calculate_grade(79.9), "C")
        self.assertEqual(calculate_grade(70), "C")

    def test_grade_D(self):
        self.assertEqual(calculate_grade(69.9), "D")
        self.assertEqual(calculate_grade(60), "D")

    def test_grade_F(self):
        self.assertEqual(calculate_grade(59.9), "F")
        self.assertEqual(calculate_grade(0), "F")

    def test_invalid_score_range(self):
        with self.assertRaises(ValueError):
            calculate_grade(-1)
        with self.assertRaises(ValueError):
            calculate_grade(101)

    def test_invalid_score_type(self):
        with self.assertRaises(TypeError):
            calculate_grade("eighty")

    def test_average_calculation(self):
        scores = [90, 80, 70]
        self.assertAlmostEqual(calculate_average(scores), 80.0)

    def test_empty_scores_average(self):
        self.assertEqual(calculate_average([]), 0.0)


if __name__ == "__main__":
    unittest.main()
