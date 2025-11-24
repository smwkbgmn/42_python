import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    """Slice a 2D array (list of lists) from start to end index.

    Args:
        family (list): A 2D array (list of lists).
        start (int): The starting index for slicing.
        end (int): The ending index for slicing.

    Returns:
        list: The sliced 2D array.
    """

    try:
        arr = np.array(family)
        return arr[start:end].tolist()

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return []