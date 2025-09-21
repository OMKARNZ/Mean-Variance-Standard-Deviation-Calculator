import unittest
from mean_var_std import calculate

class UnitTests(unittest.TestCase):
    def test_calculate_valid(self):
        result = calculate([0,1,2,3,4,5,6,7,8])
        self.assertIsInstance(result, dict)
        self.assertIn('mean', result)
        self.assertEqual(result['sum'][2], 36)

    def test_calculate_invalid(self):
        with self.assertRaises(ValueError):
            calculate([1,2,3])

if __name__ == "__main__":
    unittest.main()
