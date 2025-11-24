import math
from typing import Any


def NULL_not_found(object: Any) -> int:
    """
    Detect and print "null-like" object types.

    Null-like values include:
    - None: Python's null
    - NaN: Numerical null (missing number)
    - 0: Zero (mathematical "nothing")
    - "": Empty string (textual "nothing")
    - False: Boolean "nothing"

    Args:
        object: Any object to check

    Returns:
        0 if object is null-like (success)
        1 if object is not null-like (error/not found)
    """

    # Check for None
    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0

    # Check for NaN (must check before falsy check)
    if isinstance(object, float) and math.isnan(object):
        print(f"Cheese: {object} {type(object)}")
        return 0

    # Check for other falsy values (0, "", False)
    if not object:
        obj_type = type(object)

        # Check bool before int (bool is subclass of int)
        if obj_type is bool:
            print(f"Fake: {object} {obj_type}")
            return 0
        elif obj_type is int:
            print(f"Zero: {object} {obj_type}")
            return 0
        elif obj_type is str:
            print(f"Empty: {obj_type}")
            return 0

    # Not a recognized null-like value
    print("Type not Found")
    return 1
