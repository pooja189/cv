'''
A simple documentation for Cap
'''
import cap
import unittest
class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'mon python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Mon Python')
if __name__ == '__main__':
    unittest.main()