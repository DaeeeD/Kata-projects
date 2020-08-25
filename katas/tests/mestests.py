import unittest 
from moncode import FizzBuzz 

class FizzBuzzTest(unittest.TestCase):
    def test_print(self):
        self.assertEqual(FizzBuzz(1), 1)

    def test_print_2(self):
        self.assertEqual(FizzBuzz(2), 2)

    def  test_print_3(self):
        self.assertEqual(FizzBuzz(3), 'Fizz')

    def test_print_5(self):
        self.assertEqual(FizzBuzz(5), 'Buzz')

    def test_print_Fizz(self):
        self.assertEqual(FizzBuzz(6), 'Fizz')
        self.assertEqual(FizzBuzz(9), 'Fizz')
        self.assertEqual(FizzBuzz(63), 'Fizz')
        self.assertEqual(FizzBuzz(12), 'Fizz')

    def test_print_Buzz(self):
        self.assertEqual(FizzBuzz(10), 'Buzz')
        self.assertEqual(FizzBuzz(85), 'Buzz')
        self.assertEqual(FizzBuzz(55), 'Buzz')
    
    def test_print_FizzBuzz(self):
        self.assertEqual(FizzBuzz(15), 'FizzBuzz')
        self.assertEqual(FizzBuzz(30), 'FizzBuzz')


