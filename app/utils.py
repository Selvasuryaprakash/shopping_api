import random
import string

def generate_random_letters(n: int) -> str:
    """
    Generate a random string of n letters (uppercase and lowercase).
    
    Args:
        n (int): Number of letters to generate.
        
    Returns:
        str: Random string of letters.
    """
    letters = string.ascii_letters  # a-zA-Z
    return ''.join(random.choice(letters) for _ in range(n))
