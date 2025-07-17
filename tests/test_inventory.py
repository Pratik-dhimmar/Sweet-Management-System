import unittest
from inventory import Inventory
from models import Sweet


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

    # def test_add_duplicate_id(self):
    #     """Test adding sweet with duplicate ID raises ValueError"""
    #     self.inventory.add_sweet(self.valid_sweet)
        
    #     duplicate_sweet = Sweet(
    #         id=1,
    #         name="Different Sweet",
    #         category="Candy",
    #         price=1.99,
    #         quantity=20
    #     )
        
    #     with self.assertRaises(ValueError) as context:
    #         self.inventory.add_sweet(duplicate_sweet)
        
    #     self.assertEqual(str(context.exception), "Sweet ID already exists.")

    # def test_add_multiple_sweets(self):
    #     """Test adding multiple sweets with unique IDs"""
    #     sweet2 = Sweet(
    #         id=2,
    #         name="Gummy Bears",
    #         category="Gummies",
    #         price=1.49,
    #         quantity=100
    #     )
        
    #     self.inventory.add_sweet(self.valid_sweet)
    #     self.inventory.add_sweet(sweet2)
        
    #     self.assertEqual(len(self.inventory.sweets), 2)
    #     self.assertIn(self.valid_sweet, self.inventory.sweets)
    #     self.assertIn(sweet2, self.inventory.sweets)

    # def test_add_sweet_with_none_fields(self):
    #     """Test adding sweet with None fields raises AttributeError"""
    #     invalid_sweet = Sweet(
    #         id=None,
    #         name=None,
    #         category=None,
    #         price=None,
    #         quantity=None
    #     )
        
    #     with self.assertRaises(AttributeError):
    #         self.inventory.add_sweet(invalid_sweet)

    # def test_add_sweet_with_invalid_price(self):
    #     """Test adding sweet with negative price raises ValueError"""
    #     invalid_sweet = Sweet(
    #         id=3,
    #         name="Invalid Price Sweet",
    #         category="Test",
    #         price=-1.99,
    #         quantity=10
    #     )
        
    #     with self.assertRaises(ValueError):
    #         self.inventory.add_sweet(invalid_sweet)

    # def test_add_sweet_with_invalid_quantity(self):
    #     """Test adding sweet with negative quantity raises ValueError"""
    #     invalid_sweet = Sweet(
    #         id=4,
    #         name="Invalid Quantity Sweet",
    #         category="Test",
    #         price=1.99,
    #         quantity=-5
    #     )
        
    #     with self.assertRaises(ValueError):
    #         self.inventory.add_sweet(invalid_sweet)


if __name__ == '__main__':
    unittest.main()