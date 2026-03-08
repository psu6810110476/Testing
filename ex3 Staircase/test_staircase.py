import unittest
from unittest.mock import patch
from staircase import create_staircase

class TestStaircase(unittest.TestCase):
    
    #ทดสอบบันได 2 ชั้นด้วยตัว
    def test_give_2_with_hash(self):
        n = 2
        pattern = '#'
        expected_output = " #\n##"
        result = create_staircase(n, pattern)
        self.assertEqual(result, expected_output)

    #ทดสอบบันได 4 ชั้น
    def test_give_4_with_hash(self):
        self.assertEqual(create_staircase(4), "   #\n  ##\n ###\n####")
        
    #ทดสอบการเปลี่ยนตัวอักษรเป็น
    def test_give_1_with_star(self):
        self.assertEqual(create_staircase(1, '*'), "*")
        
    #ทดสอบ Edge Case: ใส่เลข 0 ต้องได้ค่าว่าง
    def test_give_0_should_be_empty(self):
        self.assertEqual(create_staircase(0), "")
        
    #ทดสอบ Edge Case: ใส่เลขติดลบ ต้องได้ค่าว่าง
    def test_give_negative_number(self):
        self.assertEqual(create_staircase(-5), "")

    @patch('staircase.create_staircase')
    def test_staircase_with_stub(self, mock_create_staircase):
        mock_create_staircase.return_value = "Mocked Staircase"

        result = mock_create_staircase(100)

        self.assertEqual(result, "Mocked Staircase")
        mock_create_staircase.assert_called_once_with(100)

if __name__ == '__main__':
    unittest.main()