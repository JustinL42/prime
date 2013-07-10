#!C:\Python33\python.exe
import prime3
import unittest

class test_prime_gen(unittest.TestCase):

    def setUp(self):
        prime3.reset()
        
    def test_small_list_generation(self):
        prime3.prime_gen(10)
        true_list = [2, 3, 5, 7]
        self.assertEqual(true_list, prime3.prime_list)
        
    def test_medium_list_generation(self):
        prime3.prime_gen(10000)
        primes_under_1k = 1229
        last_three = [9949, 9967, 9973]
        
        self.assertEqual(len(prime3.prime_list), primes_under_1k)
        self.assertEqual(prime3.prime_list[-3:], last_three)

    def test_large_list_generation(self):
        prime3.prime_gen(15485863)
        
        primes_under_15485863 = 1000000
        last_three = [15485849, 15485857, 15485863]
        
        self.assertEqual(len(prime3.prime_list), primes_under_15485863)
        self.assertEqual(prime3.prime_list[-3:], last_three)
        
    def test_float(self):
        prime3.prime_gen(14.7)
        true_list = [2, 3, 5, 7, 11 ,13]
        self.assertEqual(prime3.prime_list, true_list)

class test_latest_prime(unittest.TestCase):

    def setUp(self):
        prime3.reset()
        
    def test_prime(self):
        prime3.prime_gen(7)
        self.assertEqual(7, prime3.latest_prime())
        
    def test_composite(self):
        prime3.prime_gen(10)
        self.assertEqual(7, prime3.latest_prime())
        
    def test_twin_prime(self):
        prime3.prime_gen(18)
        self.assertEqual(17, prime3.latest_prime())
    
  
class test_nth_prime(unittest.TestCase):

    def setUp(self):
        prime3.reset()
        
    def test_1st_prime(self):
        self.assertEqual(2, prime3.nth_prime(1))
        
    def test_100th_prime(self):
        self.assertEqual(541, prime3.nth_prime(100))
        
    def test_float(self):
        with self.assertRaises(Exception):
            prime3.nth_prime(13.7)
    
  
class test_is_prime(unittest.TestCase):

    def setUp(self):
        prime3.reset()
        
    def test_a_prime(self):
        self.assertTrue(prime3.is_prime(541))
    
    def test_a_composite(self):
        self.assertFalse(prime3.is_prime(541*547))
        
    def test_float(self):
        with self.assertRaises(Exception):
            prime3.is_prime(13.7)

  
class test_get_ordinal(unittest.TestCase):

    def setUp(self):
        prime3.reset()
        
    def test_normal_usage(self):
        prime3.prime_gen(541)
        self.assertEqual(prime3.get_ordinal(541), 100)
    
    def test_composite_request(self):
        prime3.prime_gen(10)
        with self.assertRaises(Exception):
            prime3.get_ordinal(8)
            
    def test_float(self):
        with self.assertRaises(Exception):
            prime3.get_ordinal(13.7)

  
class test_largest_under(unittest.TestCase):

    def setUp(self):
        prime3.reset()
        
    def test_prime(self):
        self.assertEqual(541, prime3.largest_under(547))
        self.assertEqual(3, prime3.largest_under(5))
        
    def test_composite(self):
        self.assertEqual(541, prime3.largest_under(546))
        self.assertEqual(5, prime3.largest_under(6))
        
    def test_two(self):
        with self.assertRaises(Exception):
            prime3.largest_under(2)
            
    def test_float(self):
        self.assertEqual(11, prime3.largest_under(13.7))
        

class test_factorize(unittest.TestCase):

    def setUp(self):
        prime3.reset()
        
    def test_small(self):
        results = prime3.factorize(56)
        expected = {2:3, 7:1}
        self.assertEqual(results, expected)
        
    def test_large(self):
        results = prime3.factorize(295927)
        expected = {541:1, 547:1}
        self.assertEqual(results, expected)
        
    def test_prime(self):
        results = prime3.factorize(7)
        expected = {7:1}
        self.assertEqual(results, expected)
        
    def test_one(self):
        results = prime3.factorize(1)
        expected = {}
        self.assertEqual(results, expected)
        
    def test_zero(self):
        with self.assertRaises(Exception):
            prime3.factorize(0)

    def test_float(self):
        with self.assertRaises(Exception):
            prime3.factorize(13.7)
            
    def test_negative(self):
        with self.assertRaises(Exception):
            prime3.factorize(-6)
  
class test_combine(unittest.TestCase):

    def setUp(self):
        prime3.reset()
        
    def test_large(self):
        number = {541:1, 547:1}
        self.assertEqual(295927, prime3.combine(number))
        
class test_index(unittest.TestCase):
    def setUp(self):
        prime3.prime_gen(600)
        
    def test_prime(self):
        self.assertEqual(100-1, prime3.index(541))
        
    def test_composite(self):
        self.assertEqual(100-1, prime3.index(542))
        
    def test_float(self):
        self.assertEqual(100-1, prime3.index(541.5))
        
class test_reset(unittest.TestCase):
    def setUp(self):
        prime3.prime_gen(10)
        
    def test_values_reset(self):
        prime3.reset()
        self.assertEqual([2], prime3.prime_list)
        self.assertEqual(2, prime3.latest_upto)
        self.assertEqual({2:1}, prime3.ordinal_index)
        
class test_ordinal_index(unittest.TestCase):
    def setUp(self):
        prime3.reset()
        
    def test_policy_1(self):
        prime3.index_policy = 1
        prime3.largest_under(10)
        prime3.get_ordinal(13)
        prime3.is_prime(17)
        self.assertEqual({2:1, 7:4, 13:6, 17:7}, prime3.ordinal_index)
        
    def test_policy_2(self):
        prime3.index_policy = 2
        prime3.prime_gen(10)
        self.assertEqual({2:1, 3:2, 5:3, 7:4}, prime3.ordinal_index)

if __name__ == '__main__':
    unittest.main()