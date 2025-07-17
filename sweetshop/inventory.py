from sweetshop.models import Sweet


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

    """Manages inventory of sweets in the sweet shop"""

    def view_all_sweets(self):
        """
        Return a list of all sweets in inventory.
        
        Returns:
            list: A new list containing all Sweet objects in inventory.
                  Returns empty list if inventory is empty.
        """
        return list(self.sweets)  # Return a copy of the list
    