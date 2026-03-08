import unittest
from unittest.mock import patch
from two_characters import alternate

class TestTwoCharacters(unittest.TestCase):
    
    #ทดสอบกรณีที่สามารถสลับตัวอักษรได้สำเร็จ
    def test_two_characters_valid(self):
        self.assertEqual(alternate("beabeefeab"), 5)
        
    #ทดสอบกรณีที่ไม่สามารถทำได้ หรือข้อความสั้นเกินไป
    def test_two_characters_invalid(self):
        self.assertEqual(alternate("a"), 0)
        self.assertEqual(alternate("ab"), 2)
        
    #ทดสอบกรณีข้อความยาวๆ ที่มีตัวอักษรซ้ำๆ ติดกัน
    def test_two_characters_same_consecutive(self):
        self.assertEqual(alternate("asdcbsdcagfsdbgdfanfghbsfdab"), 8)

    @patch('two_characters.alternate')
    def test_two_characters_with_stub(self, mock_alternate):
        mock_alternate.return_value = 99

        result = mock_alternate("helloworld")

        self.assertEqual(result, 99)
        mock_alternate.assert_called_once_with("helloworld")

if __name__ == '__main__':
    unittest.main()