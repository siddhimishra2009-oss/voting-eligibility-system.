import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from eligibility import check_eligibility, parse_age  # noqa: E402


class TestEligibility(unittest.TestCase):
    def test_normal_input(self):  # Aman, 25, y
        self.assertEqual(check_eligibility(25, True), (True, [], 0))

    def test_boundary(self):  # Neha 18 y, Ravi 17 y
        self.assertTrue(check_eligibility(18, True)[0])
        eligible, reasons, years = check_eligibility(17, True)
        self.assertFalse(eligible)
        self.assertEqual(years, 1)

    def test_invalid_age(self):  # Amit: abc, -5, 30
        with self.assertRaises(ValueError) as e:
            parse_age("abc")
        self.assertEqual(str(e.exception), "Invalid input. Enter a whole number.")
        with self.assertRaises(ValueError) as e:
            parse_age("-5")
        self.assertEqual(str(e.exception),
                         "Invalid age. Age must be between 0 and 120.")
        self.assertEqual(parse_age("30"), 30)

    def test_not_citizen(self):  # Riya, 30, n
        eligible, reasons, years = check_eligibility(30, False)
        self.assertFalse(eligible)
        self.assertEqual(reasons, ["Not an Indian citizen."])
        self.assertEqual(years, 0)

    def test_age_limits(self):
        self.assertEqual(parse_age("0"), 0)
        self.assertEqual(parse_age("120"), 120)
        with self.assertRaises(ValueError):
            parse_age("121")
        with self.assertRaises(ValueError):
            parse_age("2.5")


if __name__ == "__main__":
    unittest.main()