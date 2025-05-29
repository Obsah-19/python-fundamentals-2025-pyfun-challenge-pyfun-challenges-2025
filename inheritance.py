class Shape:
    """Base class for geometric shapes"""
    
    def __init__(self, name: str):
        self.name = name
        
    def area(self) -> float:
        """Calculate shape area"""
        raise NotImplementedError("Subclasses must implement area()")
        
    def __str__(self) -> str:
        """Human-readable shape info"""
        return f"{self.name} with area {self.area():.2f}"


class Circle(Shape):
    """Circle implementation"""
    
    def __init__(self, radius: float):
        super().__init__("Circle")
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
        
    def area(self) -> float:
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    """Rectangle implementation"""
    
    def __init__(self, width: float, height: float):
        super().__init__("Rectangle")
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        self.width = width
        self.height = height
        
    def area(self) -> float:
        return self.width * self.height


class Triangle(Shape):
    """Triangle implementation"""
    
    def __init__(self, base: float, height: float):
        super().__init__("Triangle")
        if base <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        self.base = base
        self.height = height
        
    def area(self) -> float:
        return 0.5 * self.base * self.height
