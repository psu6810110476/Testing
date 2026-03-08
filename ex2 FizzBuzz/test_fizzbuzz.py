import unittest
from unittest.mock import patch
from fizzbuzz import get_fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    
    #ทดสอบกรณีหารลงตัวทั้ง 3 และ 5
    def test_fizzbuzz_divisible_by_3_and_5(self):
        self.assertEqual(get_fizzbuzz(15), "FizzBuzz")
        self.assertEqual(get_fizzbuzz(30), "FizzBuzz")
        
    #ทดสอบกรณีหาร 3 ลงตัวอย่างเดียว
    def test_fizzbuzz_divisible_by_3(self):
        self.assertEqual(get_fizzbuzz(9), "Fizz")
        
    #ทดสอบกรณีหาร 5 ลงตัวอย่างเดียว
    def test_fizzbuzz_divisible_by_5(self):
        self.assertEqual(get_fizzbuzz(10), "Buzz")
        
    #ทดสอบกรณีหารไม่ลงตัวเลย
    def test_fizzbuzz_not_divisible_by_3_or_5(self):
        self.assertEqual(get_fizzbuzz(7), "7")
        self.assertEqual(get_fizzbuzz(2), "2")
        
    #ทดสอบ Edge Case: เลข 0
    def test_fizzbuzz_zero(self):
        self.assertEqual(get_fizzbuzz(0), "FizzBuzz")
        
    #ทดสอบ Edge Case: เลขติดลบ
    def test_fizzbuzz_negative(self):
        self.assertEqual(get_fizzbuzz(-3), "Fizz")

    @patch('fizzbuzz.get_fizzbuzz')
    def test_fizzbuzz_with_stub(self, mock_get_fizzbuzz):
        mock_get_fizzbuzz.return_value = "MockedBuzz"

        result = mock_get_fizzbuzz(7)
        self.assertEqual(result, "MockedBuzz")
        mock_get_fizzbuzz.assert_called_once_with(7)

if __name__ == '__main__':
    unittest.main()