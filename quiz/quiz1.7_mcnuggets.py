def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    if n > 0:
        return McNuggets(n - 20) or McNuggets(n - 9) or McNuggets(n - 6)
    elif n < 0:
        return False
    else:
        return True