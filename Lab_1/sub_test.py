import calculator as c
import unittest
 
class TestSub(unittest.TestCase):
 
    def test_sub_integers_positive(self):
        result = c.sum(1, 2)
        self.assertEqual(result, 3)

    def test_sub_integers_negative(self):
        result = c.sum(-1, -2)
        self.assertEqual(result, -3)    

    def test_sub_integers_pos_neg(self):
        result = c.sum(1, -2)
        self.assertEqual(result, -1)  

    def test_sub_integers_neg_pos(self):
        result = c.sum(-1, 2)
        self.assertEqual(result, 1)  
 
 
if __name__ == '__main__':
    unittest.main()