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

class TestInventorySearchSweets(unittest.TestCase):
    """Test cases for Inventory.search_sweets() method"""

    def setUp(self):
        """Set up test inventory with sample sweets"""
        self.inventory = Inventory()
        
        # Add test sweets
        self.sweet1 = Sweet(id=1, name="Chocolate Bar", category="Chocolate", price=2.99, quantity=50)
        self.sweet2 = Sweet(id=2, name="Dark Chocolate", category="Chocolate", price=3.49, quantity=30)
        self.sweet3 = Sweet(id=3, name="Gummy Bears", category="Gummies", price=1.99, quantity=100)
        self.sweet4 = Sweet(id=4, name="Jelly Beans", category="Gummies", price=1.49, quantity=75)
        self.sweet5 = Sweet(id=5, name="Caramel Bar", category="Caramel", price=2.49, quantity=40)
        
        for sweet in [self.sweet1, self.sweet2, self.sweet3, self.sweet4, self.sweet5]:
            self.inventory.add_sweet(sweet)

    def test_search_with_no_filters(self):
        """Test search with no filters returns all sweets"""
        result = self.inventory.search_sweets()
        self.assertEqual(len(result), 5)
        self.assertCountEqual(result, [self.sweet1, self.sweet2, self.sweet3, self.sweet4, self.sweet5])

    def test_search_by_name_exact_match(self):
        """Test search by exact name (case-insensitive)"""
        result = self.inventory.search_sweets(name="Chocolate Bar")
        self.assertEqual(len(result), 1)
        self.assertIn(self.sweet1, result)

    def test_search_by_name_partial_match(self):
        """Test search by partial name (case-insensitive)"""
        result = self.inventory.search_sweets(name="choco")
        self.assertEqual(len(result), 2)
        self.assertIn(self.sweet1, result)
        self.assertIn(self.sweet2, result)

    def test_search_by_category(self):
        """Test search by exact category match"""
        result = self.inventory.search_sweets(category="Gummies")
        self.assertEqual(len(result), 2)
        self.assertIn(self.sweet3, result)
        self.assertIn(self.sweet4, result)

    def test_search_by_price_range(self):
        """Test search by price range"""
        result = self.inventory.search_sweets(min_price=2.00, max_price=3.00)
        self.assertEqual(len(result), 2)
        self.assertIn(self.sweet1, result)
        self.assertIn(self.sweet5, result)
        self.assertNotIn(self.sweet3, result)

    def test_search_combined_filters(self):
        """Test search with combined filters"""
        result = self.inventory.search_sweets(
            name="chocolate",
            category="Chocolate",
            min_price=3.00
        )
        self.assertEqual(len(result), 1)
        self.assertIn(self.sweet2, result)

    def test_search_no_matches(self):
        """Test search that returns no matches"""
        result = self.inventory.search_sweets(name="Non-existent Sweet")
        self.assertEqual(len(result), 0)

    def test_search_invalid_price_range(self):
        """Test search with invalid price range raises ValueError"""
        with self.assertRaises(ValueError):
            self.inventory.search_sweets(min_price=5.00, max_price=1.00)

    def test_search_with_none_values(self):
        """Test search handles None values correctly"""
        result = self.inventory.search_sweets(name=None, category="Gummies")
        self.assertEqual(len(result), 2)
        self.assertIn(self.sweet3, result)
        self.assertIn(self.sweet4, result)

class TestInventorySortSweets(unittest.TestCase):
    """Test cases for Inventory.sort_sweets() method"""

    def setUp(self):
        """Set up test inventory with sample sweets"""
        self.inventory = Inventory()
        
        # Add test sweets in unsorted order
        self.sweet1 = Sweet(id=1, name="Chocolate Bar", category="Chocolate", price=2.99, quantity=50)
        self.sweet2 = Sweet(id=2, name="Gummy Bears", category="Gummies", price=1.99, quantity=100)
        self.sweet3 = Sweet(id=3, name="Caramel Bar", category="Caramel", price=2.49, quantity=40)
        self.sweet4 = Sweet(id=4, name="Dark Chocolate", category="Chocolate", price=3.49, quantity=30)
        
        for sweet in [self.sweet1, self.sweet2, self.sweet3, self.sweet4]:
            self.inventory.add_sweet(sweet)

    def test_sort_by_name_ascending(self):
        """Test sorting by name in ascending order"""
        result = self.inventory.sort_sweets(key="name")
        expected_order = [self.sweet3, self.sweet1, self.sweet4, self.sweet2]
        self.assertEqual(result, expected_order)

    def test_sort_by_name_descending(self):
        """Test sorting by name in descending order"""
        result = self.inventory.sort_sweets(key="name", reverse=True)
        expected_order = [self.sweet2, self.sweet4, self.sweet1, self.sweet3]
        self.assertEqual(result, expected_order)

    def test_sort_by_category_ascending(self):
        """Test sorting by category in ascending order"""
        result = self.inventory.sort_sweets(key="category")
        expected_order = [self.sweet3, self.sweet1, self.sweet4, self.sweet2]
        self.assertEqual(result, expected_order)

    def test_sort_by_price_ascending(self):
        """Test sorting by price in ascending order"""
        result = self.inventory.sort_sweets(key="price")
        expected_order = [self.sweet2, self.sweet3, self.sweet1, self.sweet4]
        self.assertEqual(result, expected_order)

    def test_sort_by_price_descending(self):
        """Test sorting by price in descending order"""
        result = self.inventory.sort_sweets(key="price", reverse=True)
        expected_order = [self.sweet4, self.sweet1, self.sweet3, self.sweet2]
        self.assertEqual(result, expected_order)

    def test_sort_empty_inventory(self):
        """Test sorting when inventory is empty"""
        empty_inventory = Inventory()
        result = empty_inventory.sort_sweets(key="name")
        self.assertEqual(result, [])

    def test_sort_after_modification(self):
        """Test sorting after inventory modification"""
        new_sweet = Sweet(id=5, name="Apple Candy", category="Fruit", price=1.49, quantity=60)
        self.inventory.add_sweet(new_sweet)
        
        result = self.inventory.sort_sweets(key="name")
        self.assertEqual(result[0], new_sweet)  # Should be first alphabetically

    def test_sort_with_invalid_key(self):
        """Test sorting with invalid key raises ValueError"""
        with self.assertRaises(ValueError) as context:
            self.inventory.sort_sweets(key="invalid_key")
        self.assertEqual(str(context.exception), "Invalid sort key")

    def test_sort_returns_new_list(self):
        """Test that returned list is a copy, not the original"""
        original_sweets = self.inventory.sweets.copy()
        result = self.inventory.sort_sweets(key="name")
        
        # Modify the result list
        result.append(Sweet(id=99, name="Test", category="Test", price=10, quantity=0))
        
        # Original inventory should remain unchanged
        self.assertEqual(self.inventory.sweets, original_sweets)

class TestInventoryPurchaseSweet(unittest.TestCase):
    """Test cases for Inventory.purchase_sweet() method"""

    def setUp(self):
        """Set up test inventory with sample sweets"""
        self.inventory = Inventory()
        
        # Add test sweets
        self.sweet1 = Sweet(id=1, name="Chocolate Bar", category="Chocolate", price=2.99, quantity=50)
        self.sweet2 = Sweet(id=2, name="Gummy Bears", category="Gummies", price=1.99, quantity=100)
        
        self.inventory.add_sweet(self.sweet1)
        self.inventory.add_sweet(self.sweet2)

    def test_purchase_valid_quantity(self):
        """Test purchasing with valid quantity reduces stock"""
        initial_quantity = self.sweet1.quantity
        purchase_qty = 10
        
        self.inventory.purchase_sweet(self.sweet1.id, purchase_qty)
        
        self.assertEqual(self.sweet1.quantity, initial_quantity - purchase_qty)
        self.assertEqual(self.sweet2.quantity, 100)  # Other sweet unchanged

    def test_purchase_non_existent_sweet(self):
        """Test purchasing non-existent sweet raises KeyError"""
        with self.assertRaises(KeyError) as context:
            self.inventory.purchase_sweet(999, 5)
        self.assertEqual(str(context.exception), "'Sweet not found.'")

    def test_purchase_insufficient_stock(self):
        """Test purchasing more than available raises ValueError"""
        with self.assertRaises(ValueError) as context:
            self.inventory.purchase_sweet(self.sweet1.id, 100)
        self.assertEqual(str(context.exception), "Not enough stock.")

    def test_purchase_exact_quantity(self):
        """Test purchasing exact quantity reduces stock to 0"""
        self.inventory.purchase_sweet(self.sweet1.id, self.sweet1.quantity)
        self.assertEqual(self.sweet1.quantity, 0)

    def test_purchase_zero_quantity(self):
        """Test purchasing 0 quantity raises ValueError"""
        with self.assertRaises(ValueError) as context:
            self.inventory.purchase_sweet(self.sweet1.id, 0)
        self.assertEqual(str(context.exception), "Quantity must be positive.")

    def test_purchase_negative_quantity(self):
        """Test purchasing negative quantity raises ValueError"""
        with self.assertRaises(ValueError) as context:
            self.inventory.purchase_sweet(self.sweet1.id, -5)
        self.assertEqual(str(context.exception), "Quantity must be positive.")

    def test_purchase_maintains_other_sweets(self):
        """Test purchasing doesn't affect other sweets"""
        initial_sweet2_qty = self.sweet2.quantity
        self.inventory.purchase_sweet(self.sweet1.id, 10)
        self.assertEqual(self.sweet2.quantity, initial_sweet2_qty)

if __name__ == '__main__':
    unittest.main()