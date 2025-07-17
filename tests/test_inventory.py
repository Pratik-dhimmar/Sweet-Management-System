import unittest
from sweetshop.inventory import Inventory
from sweetshop.models import Sweet

class TestInventoryAddSweet(unittest.TestCase):
    """Test cases for Inventory.add_sweet() method"""

    def setUp(self):
        """Set up fresh inventory for each test"""
        self.inventory = Inventory()
        self.valid_sweet = Sweet(
            id=1,
            name="Chocolate Bar",
            category="Chocolate",
            price=2.99,
            quantity=50
        )
    

    def test_add_valid_sweet(self):
        """Test adding a valid sweet to inventory"""
        self.inventory.add_sweet(self.valid_sweet)
        self.assertIn(self.valid_sweet, self.inventory.sweets)

    def test_add_duplicate_id(self):
        """Test adding sweet with duplicate ID raises ValueError"""
        self.inventory.add_sweet(self.valid_sweet)
        
        duplicate_sweet = Sweet(
            id=1,
            name="Different Sweet",
            category="Candy",
            price=1.99,
            quantity=20
        )
        
        with self.assertRaises(ValueError) as context:
            self.inventory.add_sweet(duplicate_sweet)
        
        self.assertEqual(str(context.exception), "Sweet ID already exists.")

    def test_add_multiple_sweets(self):
        """Test adding multiple sweets with unique IDs"""
        sweet2 = Sweet(
            id=2,
            name="Gummy Bears",
            category="Gummies",
            price=1.49,
            quantity=100
        )
        
        self.inventory.add_sweet(self.valid_sweet)
        self.inventory.add_sweet(sweet2)
        
        self.assertEqual(len(self.inventory.sweets), 2)
        self.assertIn(self.valid_sweet, self.inventory.sweets)
        self.assertIn(sweet2, self.inventory.sweets)

    def test_add_sweet_with_invalid_data(self):
        """Test that invalid sweets can't be created"""
        with self.assertRaises(AttributeError):
            Sweet(
                id=None,
                name=None,
                category=None,
                price=None,
                quantity=None
            )
        
        with self.assertRaises(ValueError):
            Sweet(
                id=3,
                name="Invalid Price Sweet",
                category="Test",
                price=-1.99,
                quantity=10
            )
        
        with self.assertRaises(ValueError):
            Sweet(
                id=4,
                name="Invalid Quantity Sweet",
                category="Test",
                price=1.99,
                quantity=-5
            )

    def test_add_non_sweet_object(self):
        """Test that only Sweet objects can be added"""
        with self.assertRaises(TypeError):
            self.inventory.add_sweet("not a sweet object")

class TestInventoryDeleteSweet(unittest.TestCase):
    """Test cases for Inventory.delete_sweet() method"""

    def setUp(self):
        """Set up fresh inventory with test data for each test"""
        self.inventory = Inventory()
        
        # Add some test sweets
        self.sweet1 = Sweet(id=1, name="Chocolate Bar", category="Chocolate", price=2.99, quantity=50)
        self.sweet2 = Sweet(id=2, name="Gummy Bears", category="Gummies", price=1.49, quantity=100)
        
        self.inventory.add_sweet(self.sweet1)
        self.inventory.add_sweet(self.sweet2)

    def test_delete_existing_sweet(self):
        """Test deleting an existing sweet"""
        initial_count = len(self.inventory.sweets)
        self.inventory.delete_sweet(1)
        
        self.assertEqual(len(self.inventory.sweets), initial_count - 1)
        self.assertNotIn(self.sweet1, self.inventory.sweets)
        self.assertIn(self.sweet2, self.inventory.sweets)

    def test_delete_non_existing_sweet(self):
        """Test deleting a sweet that doesn't exist"""
        with self.assertRaises(KeyError) as context:
            self.inventory.delete_sweet(999)
        
        self.assertEqual(str(context.exception), "'Sweet not found.'")

    def test_delete_twice(self):
        """Test deleting a sweet then trying to delete it again"""
        self.inventory.delete_sweet(1)
        
        with self.assertRaises(KeyError) as context:
            self.inventory.delete_sweet(1)
        
        self.assertEqual(str(context.exception), "'Sweet not found.'")

    def test_delete_after_add(self):
        """Test sequence of add and delete operations"""
        sweet3 = Sweet(id=3, name="Lollipop", category="Hard Candy", price=0.99, quantity=75)
        self.inventory.add_sweet(sweet3)
        
        self.inventory.delete_sweet(2)
        self.inventory.delete_sweet(3)
        
        self.assertEqual(len(self.inventory.sweets), 1)
        self.assertIn(self.sweet1, self.inventory.sweets)

    def test_delete_with_invalid_id_type(self):
        """Test deleting with invalid ID type (not integer)"""
        with self.assertRaises(TypeError):
            self.inventory.delete_sweet("not_an_integer")

class TestInventoryViewAllSweets(unittest.TestCase):
    """Test cases for Inventory.view_all_sweets() method"""

    def setUp(self):
        """Set up fresh inventory for each test"""
        self.inventory = Inventory()
        self.sweet1 = Sweet(
            id=1,
            name="Chocolate Bar",
            category="Chocolate",
            price=2.99,
            quantity=50
        )
        self.sweet2 = Sweet(
            id=2,
            name="Gummy Bears",
            category="Gummies",
            price=1.49,
            quantity=100
        )

    def test_view_all_when_empty(self):
        """Test viewing all sweets when inventory is empty"""
        result = self.inventory.view_all_sweets()
        self.assertEqual(result, [])
        self.assertEqual(len(result), 0)

    def test_view_all_after_adding_sweets(self):
        """Test viewing all sweets after adding multiple sweets"""
        self.inventory.add_sweet(self.sweet1)
        self.inventory.add_sweet(self.sweet2)
        
        result = self.inventory.view_all_sweets()
        self.assertEqual(len(result), 2)
        self.assertIn(self.sweet1, result)
        self.assertIn(self.sweet2, result)

    def test_view_all_after_deletion(self):
        """Test viewing all sweets after some deletions"""
        self.inventory.add_sweet(self.sweet1)
        self.inventory.add_sweet(self.sweet2)
        self.inventory.delete_sweet(1)  # Delete sweet1
        
        result = self.inventory.view_all_sweets()
        self.assertEqual(len(result), 1)
        self.assertNotIn(self.sweet1, result)
        self.assertIn(self.sweet2, result)

    def test_view_all_returns_new_list(self):
        """Test that returned list is a copy, not the original"""
        self.inventory.add_sweet(self.sweet1)
        original_list = self.inventory.view_all_sweets()
        original_list.append(self.sweet2)  # Should not affect inventory
        
        self.assertEqual(len(self.inventory.view_all_sweets()), 1)
        self.assertNotIn(self.sweet2, self.inventory.view_all_sweets())



if __name__ == '__main__':
    unittest.main()