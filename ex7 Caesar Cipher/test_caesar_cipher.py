import unittest
from unittest.mock import patch
from caesar_cipher import caesar_cipher

class TestCaesarCipher(unittest.TestCase):
    
    #ทดสอบตัวพิมพ์เล็ก-ใหญ่ผสมกัน และมีเครื่องหมายขีด
    def test_caesar_cipher_lowercase(self):
        self.assertEqual(caesar_cipher("middle-Outz", 2), "okffng-Qwvb")
        
    #ทดสอบการวนกลับ (Wrap around) เช่น z เลื่อนไป 3 ตำแหน่งต้องวนกลับมาเป็น c
    def test_caesar_cipher_wrap_around(self):
        self.assertEqual(caesar_cipher("xyz", 3), "abc")
        
    #ทดสอบกรณีค่า k มากกว่า 26
    def test_caesar_cipher_large_k(self):
        self.assertEqual(caesar_cipher("abc", 26), "abc")
        self.assertEqual(caesar_cipher("abc", 28), "cde")

    @patch('caesar_cipher.caesar_cipher')
    def test_caesar_cipher_with_stub(self, mock_caesar):
        mock_caesar.return_value = "Hacked"

        result = mock_caesar("SecretMessage", 5)

        self.assertEqual(result, "Hacked")
        mock_caesar.assert_called_once_with("SecretMessage", 5)

if __name__ == '__main__':
    unittest.main()