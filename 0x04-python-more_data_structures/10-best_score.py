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

    # Use the max function with a lambda function as the key to find the key with the maximum value
    leader = max(a_dictionary, key=lambda k: a_dictionary[k])
    return leader

