from typing import Any
import math

def NULL_not_found(object: Any) -> int: 
    if object is None: 
        print("Nothing:", object, type(object)) 
        return 0 
    elif isinstance(object, float) and math.isnan(object): 
        print("Cheese:", object, type(object)) 
        return 0 
    elif object == 0 and not isinstance(object, bool): 
        print("Zero:", object, type(object)) 
        return 0 
    elif object == "": 
        print("Empty:", object, type(object)) 
        return 0 
    elif object is False: 
        print("Fake:", object, type(object)) 
        return 0 
    else: 
        print("Type not Found") 
    return 1