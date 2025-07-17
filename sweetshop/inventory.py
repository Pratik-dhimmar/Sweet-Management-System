from sweetshop.models import Sweet
from typing import List

class Inventory:
    """Manages inventory of sweets in the sweet shop"""
    
    def __init__(self):
        """Initialize empty inventory"""
        self.sweets = []
    
    def add_sweet(self, sweet: Sweet):
        """
        Add a sweet to the inventory.
        
        Args:
            sweet: Sweet object to add
            
        Raises:
            ValueError: If sweet ID already exists in inventory
        """
        if not isinstance(sweet, Sweet):
            raise TypeError("Can only add Sweet objects to inventory")
            
        if sweet in self.sweets:
            raise ValueError("Sweet ID already exists.")
            
        self.sweets.append(sweet)

    def delete_sweet(self, sweet_id: int):
        """
        Remove a sweet from inventory by its ID.
        
        Args:
            sweet_id: ID of the sweet to remove
            
        Raises:
            KeyError: If sweet with given ID is not found
            TypeError: If sweet_id is not an integer
        """
        if not isinstance(sweet_id, int):
            raise TypeError("Sweet ID must be an integer")
            
        for i, sweet in enumerate(self.sweets):
            if sweet.id == sweet_id:
                del self.sweets[i]
                return
        
        raise KeyError("Sweet not found.")

    def view_all_sweets(self):
        """
        Return a list of all sweets in inventory.
        
        Returns:
            list: A new list containing all Sweet objects in inventory.
                  Returns empty list if inventory is empty.
        """
        return list(self.sweets)  # Return a copy of the list

    def search_sweets(self, name=None, category=None, min_price=None, max_price=None) -> List[Sweet]:
        """
        Search sweets based on multiple filters.
        
        Args:
            name: Case-insensitive substring to search in sweet names
            category: Exact category to match
            min_price: Minimum price (inclusive)
            max_price: Maximum price (inclusive)
            
        Returns:
            List of Sweet objects matching all specified filters
            
        Raises:
            ValueError: If min_price > max_price
        """
        if min_price is not None and max_price is not None and min_price > max_price:
            raise ValueError("min_price cannot be greater than max_price")
            
        results = []
        
        for sweet in self.sweets:
            # Name filter (case-insensitive substring match)
            name_match = True
            if name is not None:
                name_match = name.lower() in sweet.name.lower()
            
            # Category filter (exact match)
            category_match = True
            if category is not None:
                category_match = category == sweet.category
            
            # Price range filter
            price_match = True
            if min_price is not None:
                price_match = sweet.price >= min_price
            if max_price is not None:
                price_match = price_match and (sweet.price <= max_price)
            
            if name_match and category_match and price_match:
                results.append(sweet)
        
        return results

if __name__ == '__main__':
    pass