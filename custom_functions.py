def format_text(
    text: str,
    prefix: str = "",
    suffix: str = "",
    capitalize: bool = False,
    max_length: int = None
) -> str:
    """
    Format text with optional prefix, suffix, capitalization, and length limit.
    
    Args:
        text: Input string to format
        prefix: Text to prepend (default "")
        suffix: Text to append (default "")
        capitalize: Capitalize entire text if True (default False)
        max_length: Truncate to this length if specified (default None)
    
    Returns:
        Formatted text string
        
    Raises:
        TypeError: If inputs are invalid type
        ValueError: If max_length is negative
        
    Examples:
        >>> format_text("hello", prefix=">>", suffix="!", capitalize=True)
        '>>HELLO!'
        >>> format_text("python", max_length=4)
        'pyth'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if max_length is not None:
        if not isinstance(max_length, int):
            raise TypeError("max_length must be integer")
        if max_length < 0:
            raise ValueError("max_length cannot be negative")
            
    result = text
    if capitalize:
        result = result.upper()
    if max_length is not None:
        result = result[:max_length]
    return prefix + result + suffix
