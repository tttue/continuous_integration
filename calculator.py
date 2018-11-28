"""
Calculator library containing basic math operations.
"""


def add(first_term=None, second_term=None):
    """Add operator

    Args:
        first_term ([int, None]):
        second_term ([int, None]):

    Returns:
        [int]:
    """
    if first_term is None or second_term is None:
        return None
    return first_term + second_term


def subtract(first_term, second_term):
    """Subtract operator

    Args:
        first_term (int):
        second_term (int):

    Returns:
        [int]:
    """
    return first_term - second_term
