import unittest
from unittest.mock import patch
from alternating_characters import alternating_characters

class TestAlternatingCharacters(unittest.TestCase):
    
    # 1. ทดสอบกรณีที่ต้องมีการลบตัวอักษรซ้ำ
    def test_alternating_chars_deletions(self):
        self.assertEqual(alternating_characters("AAAA"), 3)
        self.assertEqual(alternating_characters("BBBBB"), 4)
        
    # 2. ทดสอบกรณีที่ไม่ต้องลบเลย
    def test_alternating_chars_no_deletions(self):
        self.assertEqual(alternating_characters("ABABABAB"), 0)
        
    # 3. ทดสอบกรณีผสมกัน
    def test_alternating_chars_mixed(self):
        self.assertEqual(alternating_characters("AAABBB"), 4)

    @patch('alternating_characters.alternating_characters')
    def test_alternating_characters_with_stub(self, mock_alternating_chars):
        mock_alternating_chars.return_value = 99
        
        result = mock_alternating_chars("SOMESTRING")
        
        self.assertEqual(result, 99)
        mock_alternating_chars.assert_called_once_with("SOMESTRING")

if __name__ == '__main__':
    unittest.main()