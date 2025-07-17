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