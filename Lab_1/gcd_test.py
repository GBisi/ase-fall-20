import calculator as c
import unittest
 
class TestGcd(unittest.TestCase):
 
    def test_gcd_integers_positive(self):
        result = c.gcd(42, 40)
        self.assertEqual(result, 2)

    def test_gcd_integers_negative(self):
        result = c.gcd(-12, -6)
        self.assertEqual(result, -6)    

    def test_gcd_integers_pos_neg(self):
        result = c.gcd(24, -2)
        self.assertEqual(result, -2)  

    def test_gcd_integers_neg_pos(self):
        result = c.gcd(-10, 5)
        self.assertEqual(result, 5)  

    def test_gcd_prime(self):
        result = c.gcd(42, 5)
        self.assertEqual(result, 1)  
 
 
if __name__ == '__main__':
    unittest.main()