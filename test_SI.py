import unittest
from simple_interest import calculate_simple_interest


class TestSimpleInterest(unittest.TestCase):
    def test_basic_calculation(self):
        self.assertEqual(calculate_simple_interest(10000, 7.5, 3), 2250.0)

    def test_zero_values(self):
        self.assertEqual(calculate_simple_interest(0, 5, 2), 0.0)

    def test_negative_value_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_simple_interest(-1000, 5, 2)


if __name__ == "__main__":
    unittest.main()