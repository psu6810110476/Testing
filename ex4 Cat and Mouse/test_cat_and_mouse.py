import unittest
from unittest.mock import patch
from cat_and_mouse import cat_and_mouse

class TestCatAndMouse(unittest.TestCase):
    def test_cat_a_catches_first(self):
        # แมว A อยู่ใกล้หนูมากกว่า
        self.assertEqual(cat_and_mouse(2, 5, 3), "Cat A") 
        
    def test_cat_b_catches_first(self):
        # แมว B อยู่ใกล้หนูมากกว่า
        self.assertEqual(cat_and_mouse(1, 2, 3), "Cat B")
        
    def test_mouse_escapes_on_tie(self):
        # แมวทั้งสองตัวอยู่ห่างเท่ากัน
        self.assertEqual(cat_and_mouse(1, 3, 2), "Mouse C")
        
    def test_all_at_same_position(self):
        # ทุกตัวอยู่ที่เดียวกันหมด
        self.assertEqual(cat_and_mouse(5, 5, 5), "Mouse C")
        
    def test_cat_and_mouse_same_position(self):
        # แมว A อยู่ทับจุดเดียวกับหนู
        self.assertEqual(cat_and_mouse(4, 9, 4), "Cat A")

    @patch('cat_and_mouse.cat_and_mouse')
    def test_cat_and_mouse_with_stub(self, mock_cat_and_mouse):
        mock_cat_and_mouse.return_value = "Dog D"

        result = mock_cat_and_mouse(10, 20, 15)
        
        self.assertEqual(result, "Dog D")
        mock_cat_and_mouse.assert_called_once_with(10, 20, 15)

if __name__ == '__main__':
    unittest.main()