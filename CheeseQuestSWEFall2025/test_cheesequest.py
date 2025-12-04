import unittest
from unittest.mock import patch
from io import StringIO

from CheeseQuestSWEFall2025 import Inventory, demon_words

class TestCheeseQuest(unittest.TestCase):

    def test_inventory_initialization(self):
        """Test that a new inventory starts with the correct default values."""
        inv = Inventory()
        self.assertEqual(inv.gold, 0, "Gold should be 0 by default")
        self.assertEqual(inv.pickaxe, 0, "Pickaxe should be 0 by default")

    def test_inventory_custom_values(self):
        """Test that we can create an inventory with specific items."""
        inv = Inventory(gold=50, pickaxe=1)
        self.assertEqual(inv.gold, 50, "Gold should be 50")
        self.assertEqual(inv.pickaxe, 1, "Pickaxe should be 1")

    def test_item_types_calculation(self):
        """Test the item_types() method logic."""
        inv = Inventory(gold=100, key=1, shrubbery=5)
        count = inv.item_types()
        self.assertEqual(count, 3, "item_types should count exactly 3 types of items")

    def test_adding_items(self):
        """Test adding items (gameplay simulation)."""
        inv = Inventory()
        inv.gold += 10
        inv.lantern += 1   
        self.assertEqual(inv.gold, 10)
        self.assertEqual(inv.lantern, 1)


## mocks classes now, i would rather have it mock interfaces
class TestDemonWords(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_no_words_known(self, mock_stdout):
        """Test when player knows no words at all."""
        demon_words()
        output = mock_stdout.getvalue()
        self.assertIn("You do not know any words in Ozhkavosh.", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_known_spell(self, mock_stdout):
        """Test when player knows a spell (status = 2)."""
        import CheeseQuestSWEFall2025 as cq
        cq.spell_learn = 2  # Mark as known
        
        demon_words()
        output = mock_stdout.getvalue()
        self.assertIn("Spells:", output)
        self.assertIn("Ozh ensh", output)
        self.assertIn("I learn", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_unknown_spell(self, mock_stdout):
        """Test when player has discovered but not learned a spell (status = 1)."""
        import CheeseQuestSWEFall2025 as cq
        cq.spell_unlock = 1  # Mark as unknown/discovered
        
        demon_words()
        output = mock_stdout.getvalue()
        self.assertIn("Unknown:", output)
        self.assertIn("Ozh vo'ses sa", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_known_non_spell_word(self, mock_stdout):
        """Test when player knows a non-spell word (status = 2)."""
        import CheeseQuestSWEFall2025 as cq
        cq.word_darkness = 2  # Mark as known
        
        demon_words()
        output = mock_stdout.getvalue()
        self.assertIn("Non-spells:", output)
        self.assertIn("Darkness welcomes you", output)


if __name__ == '__main__':
    unittest.main()