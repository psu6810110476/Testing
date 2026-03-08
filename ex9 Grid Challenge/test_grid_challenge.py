import unittest
from unittest.mock import patch
from grid_challenge import grid_challenge

class TestGridChallenge(unittest.TestCase):
    
    #ทดสอบกรณีที่สามารถเรียงแนวตั้งได้สำเร็จ
    def test_grid_challenge_yes(self):
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        self.assertEqual(grid_challenge(grid), "YES")
        
    #ทดสอบกรณีที่เรียงแนวตั้งไม่ได้ 
    def test_grid_challenge_no(self):
        grid = ['mpxz', 'abcd', 'wlmf']
        self.assertEqual(grid_challenge(grid), "NO")
        
    #ทดสอบ Edge Case: กรณีที่มีแค่ตัวอักษรเดียว
    def test_grid_challenge_single_element(self):
        self.assertEqual(grid_challenge(['a']), "YES")

    @patch('grid_challenge.grid_challenge')
    def test_grid_challenge_with_stub(self, mock_grid_challenge):
        mock_grid_challenge.return_value = "MAYBE"

        test_input = ['z', 'a']
        result = mock_grid_challenge(test_input)

        self.assertEqual(result, "MAYBE")

        mock_grid_challenge.assert_called_once_with(test_input)

if __name__ == '__main__':
    unittest.main()