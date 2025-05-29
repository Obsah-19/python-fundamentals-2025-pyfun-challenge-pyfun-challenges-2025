def calculate(*args, **kwargs) -> float:
    """
    Perform calculations on arbitrary numbers using keyword operations.
    
    Args:
        *args: Numeric values to operate on
        **kwargs: Operations to apply (add, multiply, etc.)
    
    Returns:
        Result of calculation as float
        
    Raises:
        ValueError: For invalid operations or insufficient numbers
        
    Examples:
        >>> calculate(1, 2, 3, add=True)
        6.0
        >>> calculate(2, 3, multiply=True)
        6.0
    """
    if not args:
        raise ValueError("At least one number required")
    
    result = 1.0 if 'multiply' in kwargs else 0.0
    
    if 'add' in kwargs and kwargs['add']:
        result = sum(float(x) for x in args)
    elif 'multiply' in kwargs and kwargs['multiply']:
        for num in args:
            result *= float(num)
    else:
        raise ValueError("No valid operation specified")
        
    return result
