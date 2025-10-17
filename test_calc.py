import unittest
from calc import calculate_tip_amount

class TestTipCalculator(unittest.TestCase):
    
    def test_basic_tip(self):
        result = calculate_tip_amount(100, 15, 2)
        self.assertEqual(result['bill'], 100)
        self.assertEqual(result['tip'], 15)
        self.assertEqual(result['total'], 115)
        self.assertEqual(result['per_person'], 57.5)

    def test_no_split(self):
        result = calculate_tip_amount(80, 10, 1)
        self.assertEqual(result['per_person'], 88)

    def test_zero_people(self):
        result = calculate_tip_amount(50, 20, 0)
        self.assertEqual(result['per_person'], 60)

    def test_rounding(self):
        result = calculate_tip_amount(33.33, 12.5, 3)
        self.assertEqual(result['tip'], 4.17)
        self.assertEqual(result['total'], 37.50)
        self.assertEqual(result['per_person'], 12.5)

    def test_large_numbers(self):
        result = calculate_tip_amount(1000000, 18, 4)
        self.assertEqual(result['tip'], 180000)
        self.assertEqual(result['total'], 1180000)
        self.assertEqual(result['per_person'], 295000)

if __name__ == "__main__":
    unittest.main()