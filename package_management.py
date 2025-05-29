import datetime

def date_diff_in_days(date1: str, date2: str) -> int:
    """
    Calculate the difference between two dates in days.
    
    Args:
        date1: First date in YYYY-MM-DD format
        date2: Second date in YYYY-MM-DD format
    
    Returns:
        Absolute difference in days as integer
    
    Raises:
        ValueError: If date format is invalid
        
    Examples:
        >>> date_diff_in_days('2023-01-01', '2023-01-10')
        9
        >>> date_diff_in_days('2023-12-31', '2024-01-01')
        1
    """
    try:
        d1 = datetime.datetime.strptime(date1, '%Y-%m-%d').date()
        d2 = datetime.datetime.strptime(date2, '%Y-%m-%d').date()
        return abs((d2 - d1).days)
    except ValueError as e:
        raise ValueError("Invalid date format. Use YYYY-MM-DD") from e
