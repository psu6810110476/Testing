import unittest
from unittest.mock import patch
from number_utils import is_prime_list

class TestNumberUtils(unittest.TestCase):
    
    #ทดสอบกรณีตัวเลขเป็นจำนวนเฉพาะทั้งหมด
    def test_prime_numbers(self):
        self.assertEqual(is_prime_list([2, 3, 5]), [True, True, True])
        
    #ทดสอบกรณีไม่มีจำนวนเฉพาะเลย
    def test_non_prime_numbers(self):
        self.assertEqual(is_prime_list([4, 6, 8]), [False, False, False])
        
    #ทดสอบกรณีมีผสมกัน
    def test_mixed_numbers(self):
        self.assertEqual(is_prime_list([1, 2, 4]), [False, True, False])
        
    #ค่าติดลบและศูนย์
    def test_negative_and_zero(self):
        self.assertEqual(is_prime_list([-1, 0, 1]), [False, False, False])
        
    #ลิสต์ว่างเปล่า
    def test_empty_list(self):
        self.assertEqual(is_prime_list([]), [])

    @patch('number_utils.is_prime')
    def test_is_prime_list_with_stub(self, mock_is_prime):

        mock_is_prime.return_value = True

        self.assertEqual(is_prime_list([4, 6, 8]), [True, True, True])

if __name__ == '__main__':
    unittest.main()