#!/usr/bin/python3

def best_score(a_dictionary):
    """
    A function that returns a key with the biggest integer value in a dictionary.
    
    Args:
    a_dictionary (dict): The input dictionary.

    Returns:
    str or None: The key with the maximum integer value, or None if the dictionary is empty.
    """
    if not a_dictionary:  # Check if the dictionary is empty
        return None

    score = float("-inf")  # Initialize score with negative infinity
    leader = None  # Initialize leader as None

    for key, value in a_dictionary.items():
        if isinstance(value, int) and value > score:
            score = value
            leader = key

    return leader

