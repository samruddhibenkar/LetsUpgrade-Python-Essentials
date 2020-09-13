
import unittest
import check_prime_two

class testP(unittest.TestCase):
    def test_for_no1(self):
        self.assertEqual(check_prime_two.check_two(15),"not prime")

    def test_for_no2(self):
        self.assertEqual(check_prime_two.check_two(3),"prime")
        
if __name__ == "__main__":
    unittest.main()
