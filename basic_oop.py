class Product:
    """Represents a product in inventory management system"""
    
    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize product with validation.
        
        Args:
            name: Product name
            price: Unit price (must be >= 0)
            quantity: Initial stock (must be >= 0)
            
        Raises:
            ValueError: For negative price/quantity
        """
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
            
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def add_stock(self, amount: int) -> None:
        """Add inventory with validation"""
        if amount < 0:
            raise ValueError("Cannot add negative stock")
        self.quantity += amount
        
    def remove_stock(self, amount: int) -> None:
        """Remove inventory with validation"""
        if amount < 0:
            raise ValueError("Cannot remove negative stock")
        if amount > self.quantity:
            raise ValueError("Insufficient stock")
        self.quantity -= amount
        
    def total_value(self) -> float:
        """Calculate total inventory value"""
        return self.price * self.quantity
        
    def __str__(self) -> str:
        """Human-readable product info"""
        return f"{self.name}: ${self.price:.2f} × {self.quantity} units"
