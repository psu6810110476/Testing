import unittest
from unittest.mock import patch
from funny_string import funny_string

class TestFunnyString(unittest.TestCase):
    
    #ทดสอบกรณีที่เป็น Funny String
    def test_funny_string_is_funny(self):
        self.assertEqual(funny_string("acxz"), "Funny")
        
    #ทดสอบกรณีที่ไม่เป็น Funny String
    def test_funny_string_is_not_funny(self):
        self.assertEqual(funny_string("bcxz"), "Not Funny")
        
    #ทดสอบ Edge Case: กรณีตัวอักษรซ้ำกันหมด
    def test_funny_string_same_chars(self):
        self.assertEqual(funny_string("aaaa"), "Funny")

    @patch('funny_string.funny_string')
    def test_funny_string_with_stub(self, mock_funny_string):
        mock_funny_string.return_value = "Super Funny"

        result = mock_funny_string("random_text")

        self.assertEqual(result, "Super Funny")
        mock_funny_string.assert_called_once_with("random_text")

if __name__ == '__main__':
    unittest.main()