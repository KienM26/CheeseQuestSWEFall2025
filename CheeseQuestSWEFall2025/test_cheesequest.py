import unittest
# This imports your game file. 
# Since your file is named CheeseQuestSWEFall2025.py, we import that exact name.
import CheeseQuestSWEFall2025 as game

class TestGameHelpers(unittest.TestCase):

    def test_reverse_word(self):
        # We test the 'reverse' function from the 'game' module
        result = game.reverse("abc")
        self.assertEqual(result, "cba")

    def test_reverse_sentence(self):
        result = game.reverse("hello world")
        self.assertEqual(result, "dlrow olleh")

    def test_reverse_cap(self):
        result = game.reverse_cap("hello")
        self.assertEqual(result, "Olleh")

if __name__ == '__main__':
    unittest.main()
