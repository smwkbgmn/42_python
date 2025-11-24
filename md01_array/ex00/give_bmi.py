import numpy as np


def valid(obj: list[int | float]) -> None:
    """Check if the input lists are valid.

    Args:
        height (list[int | float]): Height in cm.
        weight (list[int | float]): Weight in kg.

    Returns:
        bool: True if the input lists are valid, False otherwise.
    """

    if not all(isinstance(ele, (int, float)) and not isinstance(ele, bool) for ele in obj):
        raise TypeError("List must contain only int or float values.")
    if any(ele <= 0 for ele in obj):
        raise ValueError("Value must be positive.")


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """Calculate the BMI given height in cm and weight in kg.

    Args:
        height (list[int | float]): Height in cm.
        weight (list[int | float]): Weight in kg.

    Returns:
        np.ndarray: The BMI values.
    """
    try:
        valid(height)
        valid(weight)

        return (np.array(weight) / np.array(height)**2).tolist()

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int = 25) -> list[bool]:
    """Apply a limit to the BMI values.

    Args:
        bmi (list[int | float]): The BMI values.
        limit (int, optional): The limit to apply. Defaults to 25.

    Returns:
        list[bool]: A list indicating whether each BMI value exceeds the limit.
    """

    try:
        valid(bmi)

        return np.array(bmi) > limit
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return []
