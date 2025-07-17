class Sweet:
    """Represents a sweet item in the inventory"""
    
    def __init__(self, id: int, name: str, category: str, price: float, quantity: int):
        """
        Initialize a Sweet instance.
        
        Args:
            id: Unique identifier for the sweet
            name: Name of the sweet
            category: Category of the sweet (e.g., Chocolate, Candy)
            price: Price per unit (must be positive)
            quantity: Quantity in stock (must be non-negative)
        """
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        
        self._validate()
    
    def _validate(self):
        """Validate sweet attributes"""
        if not all([self.id, self.name, self.category]):
            raise AttributeError("ID, name, and category cannot be None or empty")
        
        if self.price <= 0:
            raise ValueError("Price must be positive")
            
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")
    
    def __eq__(self, other):
        """Two sweets are equal if their IDs match"""
        if not isinstance(other, Sweet):
            return False
        return self.id == other.id