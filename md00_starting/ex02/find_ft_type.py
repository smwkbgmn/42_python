from typing import Any


def all_thing_is_obj(object: Any) -> int:
    obj_type = type(object)

    # if isinstance(object, str):
    if obj_type is str:
        print(f"{object} is in the kitchen : {obj_type}")
    # elif isinstance(object, (list, tuple, set, dict)):
    elif obj_type in (list, tuple, set, dict):
        print(f"{obj_type.__name__} : {obj_type}")
    else:
        print("Type not found")

    return 42
