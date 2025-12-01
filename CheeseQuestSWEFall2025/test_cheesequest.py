import unittest

from CheeseQuestSWEFall2025 import Inventory

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
        """Test the itemTypes() method logic."""
        inv = Inventory(gold=100, key=1, shrubbery=5)
        count = inv.itemTypes()
        self.assertEqual(count, 3, "itemTypes should count exactly 3 types of items")

    def test_adding_items(self):
        """Test adding items (gameplay simulation)."""
        inv = Inventory()
        inv.gold += 10
        inv.lantern += 1   
        self.assertEqual(inv.gold, 10)
        self.assertEqual(inv.lantern, 1)

if __name__ == '__main__':
    unittest.main()